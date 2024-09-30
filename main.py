def readFile(fileName):
    with open(fileName, 'r') as file:
        # file to string
        return file.readlines()

def my_final_grade_calculation(fileName):

    lines = readFile(fileName)
    students = {}
    for text in lines:
        line = text.strip()
        if not line:  # بررسی خط خالی
            continue  # اگر خط خالی بود، ادامه بده
        
        student_data = line.split(',')
        name = student_data[0].lower()

        scores = []
        for str_data in student_data[1:]:
            score = int(str_data.strip())
            scores.append(score)
        
        # محاسبه نمرات آزمون
        q = scores[1:7]
        q_sorted = sorted(q)  # مرتب‌سازی نمرات
        q_filtered = q_sorted[2:]  # حذف دو نمره پایین‌ترین
        q_average = sum(q_filtered) / len(q_filtered)
        q_weight = (q_average * 25) / 100  # محاسبه 25% ارزش کل نمره

        # محسابه نمرات تکلیف
        a = scores[7:10]
        a_sorted = sorted(a)  # مرتب‌سازی نمرات
        a_filtered = a_sorted[1:]  # حذف پایین‌ترین نمره
        a_average = sum(a_filtered) / len(a_filtered)
        a_weight = (a_average * 25) / 100  # محاسبه 25% ارزش کل نمره
        
        # نمره میان ترم و نهایی
        middle = scores[10]
        final = scores[11]
        mid_weight =  (middle * 25) / 100
        final_weight = (final * 25) / 100        
        # محاسبه نمره کل
        total_score = q_weight + a_weight + mid_weight + final_weight
        
        # بررسی نمره کل
        result = "fail" 
        if total_score >= 60:
            result = "pass"

        students[name] = result

    print(students)  # برای نمایش نتایج

my_final_grade_calculation("data.txt")