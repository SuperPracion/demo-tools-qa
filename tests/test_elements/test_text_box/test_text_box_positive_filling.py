def test_filling_current_address(text_box_page):
    text_box_page.input_current_address('123')


def test_filling_permanent_address(text_box_page):
    text_box_page.input_permanent_address('123')


def test_all_fields_filling(text_box_page):
    text_box_page.input_full_name('Иванов')
    text_box_page.input_email('ivanov@gmail.com')
    text_box_page.input_current_address('Moscow')
    text_box_page.input_permanent_address('SPb')


def test_output_visualization(text_box_page):
    full_name = 'Ivanov Ivan Ivanovich'
    email = 'ivanov@gmail.com'
    current_address = 'Moscow'
    permanent_address = 'SPb'

    text_box_page.input_full_name(full_name)
    text_box_page.input_email(email)
    text_box_page.input_current_address(current_address)
    text_box_page.input_permanent_address(permanent_address)
    text_box_page.submit_button_click()
    text_box_page.output_field_check_values(full_name, email, current_address, permanent_address)


def test_email_field_error(text_box_page):
    text_box_page.input_email('!')
    text_box_page.submit_button_click()
