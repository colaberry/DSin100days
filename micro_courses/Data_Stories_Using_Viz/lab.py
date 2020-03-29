import ipywidgets as widgets 
from ipywidgets import interact, interactive_output, interactive 
import yaml 

def get_data():
    with open('dataviz_lab.yml') as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        lab_dict = yaml.load(file, Loader=yaml.FullLoader)
        return lab_dict



def qtype1(options, qnum): 

    check_dict = {}

    for x in options.keys():
            key_name = str(qnum)+"_"+str(x)
            check_dict[key_name] = widgets.Checkbox(value=False,
                                             description=options[x],
                                             disabled=False,
                                             indent=False)    
    return check_dict

def qtype2(single_options, qnum2):
    output_widget = {}
    key_name = str(qnum2)+"_0"
    output_widget[key_name] = widgets.RadioButtons(
                                    options=list(single_options.values()),
                                #    value='pineapple', # Defaults to 'pineapple'
                                   layout={'width': 'max-content'}, # If the items' names are long
                                    description= " ",
                                    disabled=False
                                )

    return output_widget

        
def options_widgets(options, qnum, qtype): 
    
    all_ouput_widgets = {}
    if qtype == 0: 
        output_widget = qtype2(options, qnum)
        all_ouput_widgets.update(output_widget)
    elif qtype ==1: 
        output_widgets = qtype1(options, qnum)
        all_ouput_widgets.update(output_widgets)
    return all_ouput_widgets


def question_widget(question, select_crit): 
    if select_crit == 0: 
        select_text = ""
    elif select_crit == 1: 
        select_text = "(Choose all correct options)"
    
    question_string = "{}  {}".format(question, select_text)
    question_put = f"<b><font size='2'>{question_string}</b>"
    return widgets.HTML(value= question_put)



def get_widgets(): 
    # get data 
    lab_dict  = get_data()

    qkeys = list(lab_dict.keys())

    all_widgets = []
    new_widgets = {}
    all_answers = {}
    for x in range(0, len(lab_dict)): 
            
            single_question = lab_dict[qkeys[x]]
            
            question = single_question["question"]
            options = single_question["options"]
            qtype = int(single_question["question_type"])
            all_answers[x] = single_question["answer"]

            opt_widgets = options_widgets(options, x, qtype)
            old_widgets = opt_widgets
            new_widgets.update(old_widgets)
            
            qwidget = question_widget(question, qtype)
            all_widgets.append(qwidget)
            
            list_widgets = list(old_widgets.values())
            for x in list_widgets: 
                all_widgets.append(x)
            

    # adding submit button 
    submit_button = widgets.Button(description="Submit")
    all_widgets.append(submit_button)
    
    # create and populate output dict 
    all_outputs ={}
    all_outputs['submit_button'] = submit_button
    all_outputs['all_widgets'] = all_widgets
    all_outputs['new_widgets'] = new_widgets
    all_outputs['lab_dict'] = lab_dict
    all_outputs['all_answers'] = all_answers
    return all_outputs


def store_answers(all_answers, new_widgets): 
    # get output from the widgets 
    
    store_data = {}
    type_to_value = {list: [], float: 0.0, int: 0, str: 0}

    # initalize store data
    for qnum in all_answers.keys(): 
        ans_type = type(all_answers[qnum])
        store_data[qnum] = type_to_value[ans_type]

    for key in new_widgets:             
        key_split = key.split("_")
        q_number = int(key_split[0])

        if key_split[1] == "0": 
            answer_value = key_split[0] +"_"+str(new_widgets[key].index) 
            store_data[q_number] = new_widgets[key].value


        if new_widgets[key].value is True: 

               
            answered = new_widgets[key].description
            temp = store_data[q_number].copy()
            temp.append(answered)
            store_data[q_number] = temp 

    return store_data

def grade_answers(store_data, all_answers, lab_dict ):
    questions_answered = []
    score_assigned = {}
    type_to_value = {list: [], float: 0.0, int: 0, str: 0}

    # initalize score_assigned 
    for qnum in all_answers.keys(): 
        ans_type = type(all_answers[qnum])
        score_assigned[qnum] = type_to_value[ans_type]

    for q_num in all_answers.keys(): 
        if q_num in list(store_data.keys()): 
            questions_answered.append(q_num)

            # based on type of question do the appropriate comparison

            # type 0 is just single answer mcq 
            qkey = "q"+str(q_num)
            if lab_dict[qkey]["question_type"] == "0": 
                if store_data[q_num] == all_answers[q_num]: 
                        score_assigned[q_num] = 1.0
                else: 
                        score_assigned[q_num] = -0.25

            # type 1 which mean has multiple answers
            if lab_dict[qkey]["question_type"] == "1": 
                
                # if answer is in all_answers then give a score of 1
                # else score of -0.25
                for ans in store_data[q_num]: 
                    if ans in all_answers[q_num]: 
                        temp = score_assigned[q_num].copy()
                        temp.append(1.0)
                        score_assigned[q_num] = temp 
                    else: 
                        temp = score_assigned[q_num].copy()
                        temp.append(-0.25)
                        score_assigned[q_num] = temp 
                
             
                     

    return score_assigned

def calcuate_score(score_assigned): 
    score_calcuated = 0 
    for key in score_assigned.keys(): 
        if type(score_assigned[key]) is float: 
            score_calcuated += score_assigned[key]
        if type(score_assigned[key]) is list: 
            score_calcuated += sum(score_assigned[key])
    
    return score_calcuated


    # MAIN FUNCTION 


def  run_lab(): 
    
    all_outputs = get_widgets()

    submit_button = all_outputs['submit_button'] 
    all_widgets = all_outputs['all_widgets'] 
    new_widgets = all_outputs['new_widgets'] 
    lab_dict = all_outputs['lab_dict'] 
    all_answers = all_outputs['all_answers']


    ui = widgets.VBox(all_widgets)

    def f(**kwargs):

        return None

    output = widgets.interactive_output(f, new_widgets)
    display(ui, output)


   
    def on_button_clicked(b):
        
        with output:
            store_data = store_answers(all_answers, new_widgets)
            score_assigned = grade_answers(store_data, all_answers, lab_dict)
            calcuated_score = calcuate_score(score_assigned)

            print("your Scores: {} \n  Calculated score = {}".format(score_assigned, calcuated_score ) )
    submit_button.on_click(on_button_clicked)








