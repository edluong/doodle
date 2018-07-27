from datetime import datetime

'''
    set up variables
'''
today = datetime.now()
cur_year = int(today.year)
avg_grad_age = 22

'''
    Ask for grad year and save the results
'''
grad_year = int(input('What year did you graduated college? '));

expected_age = (cur_year - grad_year) + avg_grad_age

print('You graduated college in {}'.format(grad_year))
print('The current year is {}'.format(cur_year))

print('You are {} - {} years old.'.format(expected_age - 1,expected_age + 1))


