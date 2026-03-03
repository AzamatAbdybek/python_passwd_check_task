def has_digit(password):
	return any(each_symbol.isdigit() for  each_symbol in password)

def has_upper_letters(password):
	return any(each_symbol.isupper() for each_symbol in password)

def has_lower_letters(password):
	return any(each_symbol.islower() for each_symbol in password)

def is_very_long(password):
	return len(password) > 12

def has_symbols(password):
	return any(
		not each_symbol.isdigit() and not each_symbol.isalpha()
		for each_symbol in password
	)

def main():
    password = input('Введите пароль: ')
    score = 0

    checks = [
        has_digit,
        has_upper_letters,
        has_lower_letters,
        is_very_long,
        has_symbols
    ]

    for each_check in checks:
        if each_check(password):
            score += 2

    print(f'Рейтинг пароля: {score}')

if __name__ == "__main__":
    main()