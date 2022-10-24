#Import libs, nornir, tree visualization, etc...

#Set constants for this program, for example some CLI's use the "?" char to command context

#set up argv to pass ip adds to main in order to have a CLI to parse and create tree from

#init nornir and set up login process for the device including creds, etc...

#Begin the core logic for this program...

    #Login to device

    #Begin creation of the root of the tree, by sending the first context helping char - ("?")

    #hold the output of the first sent command in memory

    #Structure and trim this output to be saved to a nested dict structure

    #Save this iteration's top-level command and subsiquent subcommands as key/value pairs.

    #Loop through each subcommand sending the context help char, iterating over everything until tree structure is exhausted.

#Save the final completed tree containing the root, and each branch to a dict.

#Feed this dict into a tree-visualization library to get the big picture idea...