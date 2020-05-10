def ant_array(line: int):
    before_line = []
    current_line = []
    result = []

    for i in range(line):
        if i == 0:
            current_line.append(1)
        else:
            temp = 0
            count = 1
            for j in range(len(before_line)):
                if temp == 0:
                    temp = before_line[j]
                    count = 1
                elif temp != before_line[j]:
                    current_line.append(temp)
                    current_line.append(count)
                    temp = before_line[j]
                    count = 1
                else:
                    count += 1
            if temp != 0:
                current_line.append(temp)
                current_line.append(count)

        result.append(current_line)
        print(current_line)
        before_line = current_line
        current_line = []

    # print(result)


line = int(input('Line? '))
ant_array(line)
