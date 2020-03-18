import random


class Queue:
    def __init__(self):
        self.storage = []

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        if (self.size()) > 0:
            return self.storage.pop(0)
        else:
            return None

    def size(self):
        return len(self.storage)


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        # Add users

        # create a for loop
        for i in range(num_users):
            # add user to graph
            self.add_user(f"User {i+1}")

        # Create friendships

        # create a list of all possible friendships
        all_possible_friendships = []

        # create another for loop to loop over userID
        for user_id in self.users:
            # then loop over friendID from userID + 1 to the lastID + 1
            for friend_id in range(user_id + 1, self.last_id + 1):
                # append tuple of (userID, friendID) to all possible friendships list
                all_possible_friendships.append((user_id, friend_id))

        random.shuffle(all_possible_friendships)

        # create n friendships where n = avg_friendships = num_users // 2
        for i in range(num_users * avg_friendships // 2):
            friendship = all_possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

        print(all_possible_friendships)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        # create a queue
        queue = Queue()
        # enqueue user id as a list
        queue.enqueue([user_id])

        # while queue isnt empty
        while queue.size() > 0:
            # dequeue to path variable
            path = queue.dequeue()
            # set new user id to the last item in path
            new_user_id = path[-1]

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
