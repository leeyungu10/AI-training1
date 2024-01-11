from khaiii import Khaiii

def foreigner_style_korean(input_text):
    khaiii = Khaiii()
    sentences = input_text.split('\n')

    foreigner_style_text = ""

    for sentence in sentences:
        tokens = khaiii.analyze(sentence)

        for block in tokens:
            for morph in block.morphs:
                # 여기에서 외국인 스타일 처리 로직을 추가하세요
                # 예를 들어, 명사를 특정한 단어로 대체하거나 다른 표현으로 바꾸는 등
                if morph.tag.startswith('N'):
                    morph.lex = "foreign_noun"
                foreigner_style_text += morph.lex + " "

    return foreigner_style_text.strip()

# 테스트
user_input = input("한국어를 입력하세요: ")
output_text = foreigner_style_korean(user_input)
print("외국인 스타일 한국어:", output_text)
