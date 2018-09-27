import bisect

class TopVotedCandidate:

    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        """
        self.leads = []
        self.times = times
        count = {}
        lead = -1
        for i in persons:
            count[i] = count.get(i, 0) + 1
            if count[i] >= count.get(lead, 0):
                lead = i
            self.leads.append(lead)

    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        return self.leads[bisect.bisect(self.times, t)-1]
        
def main():
    persons = [0,1,1,0,0,1,0]
    times = [0,5,10,15,20,25,30]
    test = TopVotedCandidate(persons, times)
    result = test.q(25)
    print(result)


if __name__ == '__main__':
    main()

# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)