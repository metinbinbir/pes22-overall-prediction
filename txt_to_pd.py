import pandas as pd
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

def is_integer(string):
    if string[0] == ('-', '+'):
        return string[1:].isdigit()
    else:
        return string.isdigit()

def txt_to_dataframe(filename):
    file_content_list = open(filename,"r",encoding="utf-8").read().splitlines()
    only_data_list = [x for x in file_content_list if "Position Player Name" not in x]
    columns = ["Position", "Height", "Weight", "Age", "Preferred Foot", "Avg Ball", "Avg Pass", "Finishing", "Speed",
               "Kicking Power", "Stamina", "Avg Def", "Weak Foot", "Overall"]
    df = pd.DataFrame(columns=columns)
    for row in only_data_list:
        # print(row)
        splitted_attributes = row.split(" ")
        position = splitted_attributes[0]

        for i in range(len(splitted_attributes)):
            if is_integer(splitted_attributes[i]):
                curr_index = i
                break
        row_values = []
        row_values.append(position)
        height = int(splitted_attributes[curr_index])
        row_values.append(height)
        try:
            weight = int(splitted_attributes[curr_index+1])
        except ValueError:
            continue
        row_values.append(weight)

        age = int(splitted_attributes[curr_index+2])
        row_values.append(age)

        preferred_foot = splitted_attributes[curr_index +3]
        row_values.append(preferred_foot)

        ball_control = int(splitted_attributes[curr_index+5])
        dribbling = int(splitted_attributes[curr_index+6])
        avg_ball = (ball_control + dribbling) / 2
        row_values.append(avg_ball)

        low_pass = int(splitted_attributes[curr_index+7])
        lofted_pass = int(splitted_attributes[curr_index+8])
        pass_avg = (low_pass + lofted_pass) / 2
        row_values.append(pass_avg)

        finishing = int(splitted_attributes[curr_index+9])
        row_values.append(finishing)

        speed = int(splitted_attributes[curr_index+10])
        row_values.append(speed)

        kicking_power = int(splitted_attributes[curr_index+11])
        row_values.append(kicking_power)

        stamina = int(splitted_attributes[curr_index+12])
        row_values.append(stamina)

        tackling = int(splitted_attributes[curr_index+13])
        aggression = int(splitted_attributes[curr_index+14])
        def_engagement = int(splitted_attributes[curr_index+15])
        def_avg = (tackling+aggression+def_engagement)/3
        row_values.append(def_avg)

        weak_foot = splitted_attributes[curr_index+16]
        row_values.append(weak_foot)

        overall = int(splitted_attributes[-1])
        row_values.append(overall)

        df = df.append(pd.DataFrame([row_values], columns=columns))


    df.to_csv("data.csv",encoding="utf-8",index=False)

txt_to_dataframe("player_and_stats.txt")