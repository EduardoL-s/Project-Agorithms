def study_schedule(permanence_period, target_time):
    if (type(target_time) != int):
        return None
    students = list(range(len(permanence_period)))
    total = 0
    for item in students:
        if (type(permanence_period[item][0]) != int
            or type(permanence_period[item][1]) != int):
            return None

        if (target_time in
             list(range(permanence_period[item][0], permanence_period[item][1] + 1))):
            total += 1

    return total
