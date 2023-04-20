def evaluate_expression(expression): #İşlemi hesaplamak için ana fonksiyondur. Bu fonksiyon, verilen matematiksel ifadeyi (string) değerlendirir ve sonucu döndürür.
    def apply_operator(operators, values): # Verilen operatörü (toplama, çıkarma, çarpma, bölme, üs alma veya mod alma) uygun değerlere uygular ve sonucu değerler listesine ekler.
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == '+':
            values.append(left + right)
        elif operator == '-':
            values.append(left - right)
        elif operator == '*':
            values.append(left * right)
        elif operator == '/':
            values.append(left / right)
        elif operator == '|':
            values.append(left ** right)
        elif operator == '%':
            values.append(left % right)

    def greater_precedence(op1, op2):# İki operatörün önceliğini karşılaştırır ve ilk operatörün ikincisinden daha yüksek bir önceliği olup   olmadığını kontrol eder. Öncelik, işlem sırasını belirler (örneğin, çarpma ve bölme toplama ve çıkarmadan önce yapılır).
        precedences = {'+': 1, '-': 1, '*': 2, '/': 2, '|': 3, '%': 3}
        return precedences[op1] > precedences[op2]

    operators = []
    values = []
    i = 0
    while i < len(expression):
        if expression[i] == ' ':
            i += 1
            continue
        if expression[i] in '0123456789':
            j = i
            while j < len(expression) and expression[j] in '0123456789':
                j += 1
            values.append(float(expression[i:j]))
            i = j
        elif expression[i] in "+-*/|%":
            while (operators and operators[-1] in "+-*/|%" and
                   greater_precedence(operators[-1], expression[i])):
                apply_operator(operators, values)
            operators.append(expression[i])
            i += 1
        elif expression[i] == '(':
            operators.append(expression[i])
            i += 1
        elif expression[i] == ')':
            while operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()
            i += 1
    while operators:
        apply_operator(operators, values)

    return values[0]

if __name__ == "__main__":
    islem = input("\n\n**********HOŞ GELDİNİZ********** \nToplama +\nÇıkarma -\nÇarpma *\nBölme /\nÜs alma |\nMod alma %\n\nLütfen İşlemi Giriniz ")
    sonuc = evaluate_expression(islem)
    print(f"İşlem Sonucu = {sonuc}")
