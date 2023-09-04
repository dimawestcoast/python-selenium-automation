from behave import then

@then('Verify blog is opened')
def verify_blog_opened(context):
    context.app.blog.verify_opened()

@then('Close blog')
def close_blog(context):
    context.app.blog.close_page()

@then('Return to the original window')
def return_to_original_window():
    context.app.blog.swith_to_window(context.original_window)