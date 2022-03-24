def word_count(l):
    t = []
    s ={}
    t = l.split(" ")
    for i in t:
        if not s.get(i, False):
            s[i] = 1
        else:
            s[i] = s[i] + 1
    return s 
l2 = "Lorem ipsum dolor sit amet. In world make a world to friend person to bikes want you want prefer. You hello person I much normal do bikes make of have world. Friend that to world want ask world have in rides world.In make prefer to people people me normal world in that much! To have be friend normal you bikes that. Be world want do this friend a world normal of person make. I people prefer do that i much hello do rides make do normal friend you this people.Be make bikes i hello that you hello have i want hello of want prefer ask rides prefer that that. Ask hello people me want that in want people you have hello me world have a rides that of that that. You world bikes in have this you normal rides? A friend this be want world I rides this to bikes friend to people people!"

print(word_count(l2))