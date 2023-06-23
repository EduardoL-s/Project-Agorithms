def study_schedule(permanence_period, target_time):
    if (type(target_time) != int):
        return None
    students = list(range(len(permanence_period)))
    total = 0
    for item in students:
        register = permanence_period[item]
        if (type(register[0]) != int
            or type(register[1]) != int):
            return None

        if (target_time in
         list(range(register[0], register[1] + 1))):
            total += 1

    return total
