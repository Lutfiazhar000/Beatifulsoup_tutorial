from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')

    # print(soup.prettify())
    # courses_html_tags = soup.find_all('h5')
    # for course in courses_html_tags:
    #    print(course.text)

    course_card = soup.find_all('div', class_='card')
    for course in course_card:
        
        course_name = course.h5.text
        course_price = course.a.text
        course_price_2 = course.a.text.split()[-1]

        # print(course_name)
        # print(course_price)
        print(f'{course_name} costs {course_price_2}')

        












