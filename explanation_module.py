"""
EduGenie - Concept Explanation Module

Uses the local LaMini-Flan-T5-783M model for
student-friendly concept explanations.
"""

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

from model_config import LOCAL_EXPLANATION_MODEL


# ============================================================
# LOAD LOCAL LAMINI MODEL
# ============================================================

tokenizer = AutoTokenizer.from_pretrained(
    LOCAL_EXPLANATION_MODEL
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    LOCAL_EXPLANATION_MODEL
)


# ============================================================
# CONCEPT EXPLANATION
# ============================================================

def explain_concept(concept: str, context: str = "") -> str:
    """
    Explain an educational concept using local LaMini.
    """

    if not concept or not concept.strip():
        raise ValueError("Concept cannot be empty.")

    concept = concept.strip()

    if len(concept) > 300:
        raise ValueError(
            "Concept is too long. Maximum length is 300 characters."
        )

    context = context.strip()

    if len(context) > 500:
        raise ValueError(
            "Context is too long. Maximum length is 500 characters."
        )


    # ========================================================
    # BUILD PROMPT
    # ========================================================

    if context:
        prompt = (
            f"Explain the computer science concept '{concept}' "
            f"to a college student in simple and accurate language. "
            f"First define the concept. Then explain how it works. "
            f"Then give one correct and relevant example. "
            f"Use this context only if it is relevant: {context}. "
            f"Stay focused specifically on '{concept}'."
        )

    else:
        prompt = (
            f"Explain the computer science concept '{concept}' "
            f"to a college student in simple and accurate language. "
            f"First define the concept. "
            f"Then explain how it works. "
            f"Then give one correct and relevant example. "
            f"Stay focused specifically on '{concept}'."
        )


    # ========================================================
    # TOKENIZE INPUT
    # ========================================================

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        truncation=True,
        max_length=512,
    )


    # ========================================================
    # GENERATE EXPLANATION
    # ========================================================

    outputs = model.generate(
        **inputs,
        max_new_tokens=250,
        do_sample=True,
        temperature=0.5,
        top_p=0.9,
    )


    # ========================================================
    # DECODE RESPONSE
    # ========================================================

    explanation = tokenizer.decode(
        outputs[0],
        skip_special_tokens=True,
    ).strip()


    # ========================================================
    # VALIDATE RESPONSE
    # ========================================================

    if not explanation:
        raise RuntimeError(
            "LaMini returned an empty explanation."
        )

    return explanation