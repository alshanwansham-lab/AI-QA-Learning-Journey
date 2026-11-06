# اختبار آلي بسيط للتحقق من جودة مخرجات نظام ذكاء اصطناعي (AI QA Validation)

def validate_llm_response(response_text):
    """دالة تفحص ما إذا كان رد النموذج يحتوي على إجابة ولا يحتوي على أخطاء"""
    if not response_text or "Error" in response_text:
        return False
    return True

def test_valid_response():
    # محاكاة لرد صحيح من نموذج LLM
    ai_output = "الذكاء الاصطناعي يساهم في أتمتة اختبار البرمجيات."
    assert validate_llm_response(ai_output) == True

def test_invalid_response():
    # محاكاة لرد يحتوي على خطأ
    ai_output = "Error: Model failed to process input."
    assert validate_llm_response(ai_output) == False