import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states =[]
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state== "Exit":
        missing_states=[]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        if answer_state not in guessed_states: #duping the same element caused the list to append regardlessly
                                               #so far this line solves this problem by not letting it append
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x),int(state_data.y))
            t.write(state_data.state.item())

#!!!!MY ATTEMPT
#global answer_state
#def ask_state_once_more():
#    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
#    return answer_state
#
#states_name=pandas.read_csv("50_states.csv")
#if answer_state == states_name["state"]:
#    ask_state_once_more()
#!!!MY ATTEMPT ENDS HERE
# def get_mouse_click_coor(x,y): an auxillary function to track the states position in the image by clicking
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


screen.exitonclick()