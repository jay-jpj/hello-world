#print('hello world')
type_of_exercise_done=input('what activity did you do today!')
exercise_time_period=float(input('enter the number of hours you did this activity for'))
if type_of_exercise_done=='cycling':
	pace_at_which_cycling_done=float(input('enter cycling average speed in km/h'))
	if pace_at_which_cycling_done<10:
		calories_burnt_in_one_hour=300
	elif 10<pace_at_which_cycling_done<20:
		calories_burnt_in_one_hour=450
    else:
	    calories_burnt_in_one_hour=300*(pace_at_which_cycling_done)*0.1
    total_calories_burnt=(calories_burnt_in_one_hour)*(exercise_time_period)
    print('you just burned ',total_calories_burnt,'calories')
elif type_of_exercise_done=='football':
    enter_mode=input('enter the mode in which you play:light_exercise_mode or sport_carrer_mode')
    if enter_mode=="light_exercise_mode":
        calories_burnt_in_one_hour=400
    else:
        calories_burnt_in_one_hour=750
    total_calories_burnt=(calories_burnt_in_one_hour)*(exercise_time_period)
    print('you just burned ',total_calories_burnt,'calories')
elif type_of_exercise_done=='cricket':
    enter_mode=enter_mode=input('enter the mode in which you play:light_exercise_mode or sport_carrer_mode')
    if enter_mode=="light_exercise_mode":
        calories_burnt_in_one_hour=300
    else:
        calories_burnt_in_one_hour=600
    total_calories_burnt=(calories_burnt_in_one_hour)*(exercise_time_period)
    print('you just burned ',total_calories_burnt,'calories')
elif type_of_exercise_done=='hockey':
    enter_mode=enter_mode=input('enter the mode in which you play:light_exercise_mode or sport_carrer_mode')
    if enter_mode=="light_exercise_mode":
        calories_burnt_in_one_hour=370
    else:
        calories_burnt_in_one_hour=720
    total_calories_burnt=(calories_burnt_in_one_hour)*(exercise_time_period)
    print('you just burned ',total_calories_burnt,'calories')
elif type_of_exercise_done=='basketball':
    enter_mode=enter_mode=input('enter the mode in which you play:light_exercise_mode or sport_carrer_mode')
    if enter_mode=="light_exercise_mode":
        calories_burnt_in_one_hour=500
    else:
        calories_burnt_in_one_hour=900
    total_calories_burnt=(calories_burnt_in_one_hour)*(exercise_time_period)
    print('you just burned ',total_calories_burnt,'calories')
elif type_of_exercise_done=='badminton':
    enter_mode=enter_mode=input('enter the mode in which you play:light_exercise_mode or sport_carrer_mode')
    if enter_mode=="light_exercise_mode":
        calories_burnt_in_one_hour=360
    else:
        calories_burnt_in_one_hour=580
    total_calories_burnt=(calories_burnt_in_one_hour)*(exercise_time_period)
    print('you just burned ',total_calories_burnt,'calories')
elif type_of_exercise_done=='lawn tennis':
    enter_mode=enter_mode=input('enter the mode in which you play:light_exercise_mode or sport_carrer_mode')
    if enter_mode=="light_exercise_mode":
        calories_burnt_in_one_hour=540
    else:
        calories_burnt_in_one_hour=920
    total_calories_burnt=(calories_burnt_in_one_hour)*(exercise_time_period)
    print('you just burned ',total_calories_burnt,'calories')
elif type_of_exercise_done=='table tennis':
    enter_mode=enter_mode=input('enter the mode in which you play:light_exercise_mode or sport_carrer_mode')
    if enter_mode=="light_exercise_mode":
        calories_burnt_in_one_hour=200
    else:
        calories_burnt_in_one_hour=370
    total_calories_burnt=(calories_burnt_in_one_hour)*(exercise_time_period)
    print('you just burned ',total_calories_burnt,'calories')
elif type_of_exercise_done=='swimming':
    enter_mode=enter_mode=input('enter the mode in which you swam:light_exercise_mode or heavy_intensity_mode')
    if enter_mode='light_exercise_mode':
        calories_burnt_in_one_hour=400
    else:
        calories_burnt_in_one_hour=870
    total_calories_burnt=(calories_burnt_in_one_hour)*(exercise_time_period)
    print('you just burned ',total_calories_burnt,'calories')
elif type_of_exercise_done=='jogging':
    pace_at_which_jogging_done=float(input('enter jogging average speed in km/h'))
    if pace_at_which_jogging_done<5:
        calories_burnt_in_one_hour=300
    elif 5<pace_at_which_cycling_done<12:
        calories_burnt_in_one_hour=450
    else:
        calories_burnt_in_one_hour=375*(pace_at_which_cycling_done)*0.1
    total_calories_burnt=(calories_burnt_in_one_hour)*(exercise_time_period)
    print('you just burned ',total_calories_burnt,'calories')
elif type_of_exercise_done=='walking':
        pace_at_which_walking_done=float(input('enter jogging average speed in km/h'))
        if pace_at_which_walking_done<4:
            calories_burnt_in_one_hour=200
        elif 5<pace_at_which_walking_done<10:
            calories_burnt_in_one_hour=300
        else:
            calories_burnt_in_one_hour=300*(pace_at_which_cycling_done)*0.1
        total_calories_burnt=(calories_burnt_in_one_hour)*(exercise_time_period)
        print('you just burned ',total_calories_burnt,'calories')
elif type_of_exercise_done=='sprinting':
    pace_at_which_sprinting_done=float(input('enter sprinting average speed in km/h'))
    if 15<pace_at_which_sprinting_done<20:
        calories_burnt_in_one_hour=2000
    elif 20<=pace_at_which_cycling_done<30:
        calories_burnt_in_one_hour=3500
    else:
        calories_burnt_in_one_hour=375*(pace_at_which_cycling_done)*0.1
    total_calories_burnt=(calories_burnt_in_one_hour)*(exercise_time_period)
    print('you just burned ',total_calories_burnt,'calories')
elif type_of_exercise_done=='gym workout':
    enter_mode=enter_mode=input('enter the mode in which you swam:light_exercise_mode or heavy_intensity_mode')
    if enter_mode='light_exercise_mode':
        calories_burnt_in_one_hour=300
    else:
        calories_burnt_in_one_hour=550
    total_calories_burnt=(calories_burnt_in_one_hour)*(exercise_time_period)
    print('you just burned ',total_calories_burnt,'calories')
