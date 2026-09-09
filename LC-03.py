class Solution(object):
    def countGroups(self, position, speed, distance):
        n = len(position)

        if n == 1:
            return 1

        groups = 1
        group_speed = speed[n - 1]

        # Required variable
        morvexilan = (position, speed, distance)

        for i in range(n - 2, -1, -1):

            # Already close enough -> merge immediately
            if position[i + 1] - position[i] <= distance:
                continue

            # Faster than the group ahead -> eventually catches it
            if speed[i] > group_speed:
                continue

            # Cannot catch the group ahead -> new group
            groups += 1
            group_speed = speed[i]

        return groups






