from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

from utils.validator import check_missing_values
from utils.anomaly import detect_anomalies
from utils.trustscore import calculate_trust_score
from utils.duplicates import detect_duplicates
from utils.insights import generate_insights
from utils.consistency import check_consistency
from utils.model_compare import compare_models
from utils.risk import calculate_risk
from utils.recommendations import generate_recommendations
from utils.hallucination import detect_hallucinations
from utils.grade import generate_grade
from utils.confidence import calculate_confidence
from utils.health import data_health_status
from utils.drift import detect_drift
from utils.bias import detect_bias
from utils.claim_validator import validate_claim
from utils.observation_generator import generate_observations
from utils.confidence_validator import validate_claim_confidence
from utils.statistics_validator import statistical_claim_verifier
from utils.contradiction_detector import detect_contradictions
from utils.exaggeration_detector import detect_exaggeration
from utils.evidence_checker import evaluate_evidence
from utils.relationship_discovery import discover_relationships
from utils.final_verdict import generate_final_verdict
from utils.model_output_auditor import audit_model_outputs
from utils.mode_detector import detect_mode

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def read_uploaded_file(file):
    if file.filename.endswith(".csv"):
        return pd.read_csv(file.file)

    elif file.filename.endswith(".xlsx"):
        return pd.read_excel(file.file)

    else:
        return None


def dataset_audit(df):

    missing = check_missing_values(df)
    anomalies = detect_anomalies(df)
    duplicates = detect_duplicates(df)
    consistency_issues = check_consistency(df)

    trust_score = calculate_trust_score(
        missing,
        anomalies
    )

    risk_level = calculate_risk(trust_score)
    grade = generate_grade(trust_score)

    confidence = calculate_confidence(
        trust_score,
        anomalies,
        duplicates
    )

    health_status = data_health_status(
        trust_score,
        anomalies
    )

    drift_results = detect_drift(df)
    bias_results = detect_bias(df)
    relationship_results = discover_relationships(df)

    insights = generate_insights(
        missing,
        anomalies,
        duplicates
    )

    recommendations = generate_recommendations(
        missing,
        duplicates,
        anomalies,
        trust_score
    )

    return {
        "mode": "dataset_audit",
        "columns": list(df.columns),
        "rows": len(df),
        "missing_values": missing,
        "anomalies_detected": anomalies,
        "duplicates": duplicates,
        "trust_score": trust_score,
        "risk_level": risk_level,
        "grade": grade,
        "confidence": confidence,
        "health_status": health_status,
        "consistency_issues": consistency_issues,
        "drift_detection": drift_results,
        "bias_detection": bias_results,
        "relationships": relationship_results,
        "insights": insights,
        "recommendations": recommendations
    }


def ai_output_audit(df):

    hallucination_results = detect_hallucinations(
        """
        India has 40 states.
        This model is 100% accurate.
        """
    )

    generated_observations = generate_observations(df)

    contradiction_results = detect_contradictions(
        generated_observations
    )

    statistical_results = statistical_claim_verifier(
        df,
        "Higher fare increases survival"
    )

    claim_validation_results = []

    for observation in generated_observations:

        validation = validate_claim(
            df,
            observation
        )

        support_score = validation[0].get(
            "support_score",
            50
        )

        ai_confidence = 95

        confidence_verdict = validate_claim_confidence(
            observation,
            ai_confidence,
            support_score
        )

        exaggeration_result = detect_exaggeration(
            observation,
            support_score
        )

        evidence_result = evaluate_evidence(
            support_score
        )

        claim_validation_results.append({
            "claim": observation,
            "ai_confidence": ai_confidence,
            "validation": validation,
            "confidence_verdict": confidence_verdict,
            "exaggeration": exaggeration_result,
            "evidence": evidence_result
        })

    weak_evidence_count = 0
    overconfident_count = 0

    for item in claim_validation_results:

        if item["evidence"]["evidence_level"] == "Weak Evidence":
            weak_evidence_count += 1

        if "overconfident" in item["confidence_verdict"].lower():
            overconfident_count += 1

    return {
        "hallucinations": hallucination_results,
        "generated_observations": generated_observations,
        "contradictions": contradiction_results,
        "statistical_verification": statistical_results,
        "claim_validation": claim_validation_results,
        "weak_evidence_count": weak_evidence_count,
        "overconfident_count": overconfident_count
    }


@app.get("/")
def home():
    return {
        "message": "RealityCheck AI Running"
    }


@app.post("/upload-dataset")
async def upload_dataset(
    file: UploadFile = File(...)
):

    df = read_uploaded_file(file)

    if df is None:
        return {
            "error": "Unsupported file format"
        }

    return dataset_audit(df)


@app.post("/upload-model-output")
async def upload_model_output(
    file: UploadFile = File(...)
):

    df = read_uploaded_file(file)

    if df is None:
        return {
            "error": "Unsupported file format"
        }

    model_output_audit = audit_model_outputs(df)

    return {
        "mode": "model_output_audit",
        "columns": list(df.columns),
        "rows": len(df),
        "model_output_audit": model_output_audit
    }


@app.post("/upload-combined")
async def upload_combined(
    dataset_file: UploadFile = File(...),
    model_output_file: UploadFile = File(...)
):

    dataset_df = read_uploaded_file(dataset_file)
    model_df = read_uploaded_file(model_output_file)

    if dataset_df is None or model_df is None:
        return {
            "error": "Unsupported file format"
        }

    dataset_results = dataset_audit(dataset_df)
    output_results = audit_model_outputs(model_df)
    ai_audit_results = ai_output_audit(dataset_df)

    final_verdict = generate_final_verdict(
        ai_audit_results["contradictions"],
        ai_audit_results["hallucinations"],
        dataset_results["trust_score"],
        ai_audit_results["weak_evidence_count"],
        ai_audit_results["overconfident_count"]
    )

    return {
        "mode": "combined_audit",
        "dataset_audit": dataset_results,
        "model_output_audit": output_results,
        "ai_output_audit": ai_audit_results,
        "final_verdict": final_verdict
    }


@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):

    df = read_uploaded_file(file)

    if df is None:
        return {
            "error": "Unsupported file format"
        }

    mode = detect_mode(df)

    if mode == "model_output":

        return {
            "mode": "model_output_audit",
            "columns": list(df.columns),
            "rows": len(df),
            "model_output_audit": audit_model_outputs(df)
        }

    dataset_results = dataset_audit(df)
    ai_audit_results = ai_output_audit(df)

    final_verdict = generate_final_verdict(
        ai_audit_results["contradictions"],
        ai_audit_results["hallucinations"],
        dataset_results["trust_score"],
        ai_audit_results["weak_evidence_count"],
        ai_audit_results["overconfident_count"]
    )

    return {
        **dataset_results,
        **ai_audit_results,
        "final_verdict": final_verdict
    }