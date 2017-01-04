
action_flags = {"no":1, "show":2, "clear":3,}

# print action_flags
action = 0

action_flags2 = ["", "no", "show", "clear"]
print action_flags2

command = raw_input("Prom>")

print command

if "show" in command:
    print "show in command"

else:
    print "show not in command"

# if command.split()[0] == "no":
#     print "no"
#     command = command
# elif command.split()[0] == "show":
#     print "show"
# elif command.split()[0] == "clear":
#     print "clear"

# cmd = command.split()
# print "command is:", command

# print "cmd is:", cmd

# # for use with dictionary
# if cmd[0] in action_flags:
#     print "in action_flags"
#     action =  action_flags[cmd[0]]
#     print action
# else:
#     print action

# for idx, item in enumerate(action_flags2):
#     # print idx, item

#     if cmd[0] == item:
#         action = idx
#         cmd.pop(0)
#         print cmd
 

# print action
# if action == 0:
#     new_cmd = cmd[0]
# else:
#     new_cmd = action_flags2[action]+ "-" + cmd[0]
# print "new_cmd", new_cmd
# print "cmd", cmd

