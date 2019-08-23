
PRINT_BRYCE = 1
HALT = 2
PRINT_NUM = 3
PRINT_SUM = 4
SAVE = 5
ADD = 6

memory = [
    PRINT_BRYCE,
    PRINT_NUM,
    45,
    PRINT_SUM,
    10,
    32,
    SAVE,
    2,
    99,
    SAVE,
    3,
    1,
    ADD,
    2,
    3,
    HALT
]

registers = [0] * 8

PC = 0
running = True

while running:
    command = memory[PC]

    if command == PRINT_BRYCE:
        print('Bryce!')
        PC += 1

    elif command == PRINT_NUM:
        num = memory[PC + 1]
        print(num)
        PC += 2

    elif command == PRINT_SUM:
        first_number = memory[PC + 1]
        second_number = memory[PC + 2]
        print(first_number + second_number)
        PC += 3

    elif command == SAVE:
        register = memory[PC + 1]
        number_to_save = memory[PC + 2]
        registers[register] = number_to_save
        PC += 3

    elif command == ADD:
        first_register = memory[PC + 1]
        second_register = memory[PC + 2]
        sum = registers[first_register] + registers[second_register]
        registers[first_register] = sum
        PC += 3

    elif command == HALT:
        running = False

    else:
        print('command not recognized: {}'.format(command))
        running = False
