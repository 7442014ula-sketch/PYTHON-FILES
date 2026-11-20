name = input("enter your real name, Agent: ")
gadget = input("enter your favourite gadget: ")
agent_Number = 7
speed_rating  9.5
mission_count = 12
height_m = 1.65
is_active = true

print("name:", name "-> type:", type(name))
print("gadget:", gadget, "-> type", type(gadget))
print("agent Number ", agent_Number, "-> type:", type(agent_Number))
print("speed Rating:", speed_rating, "-> type", type(speed_rating))
print("Mission count:", mission_count, "-> type", type(mission_count))
print("is active:", is_active, "-> type", type(is_active))

agent_Number_text = str(agent_Number)
mission_count_text = str(mission_count)
speed_rating_text = str(speed_rating)
status_text = str(is_active)

print("agent Number as text: ", agent_Number_text, "-> type:" type(agent_Number_text))
print("Mission count as text: ", mission_count_text, "-> type:" type(mission_count_text))
print("speed Rating as text: ", speed_rating_text, "-> type:" type(speed_rating_text))
print("status as text: ", status_text, "-> type:" type(status_text))

first_three = name[0:3]
last_letter = name[-1:]
code_name = first_three + last_letter
print("first 3 letters of name:", first_three)

reversed_gadget = gadget[::-1]
print("reversed gadget name:" , reversed_gadget)

badge_line_1 = "agent" + code_name.upper()
badge_line_2 = "id" + agent_Number_text + " | mission" + mission_count_text
badge_line_3 = "speed" + speed_rating_text + " | active" + status_text