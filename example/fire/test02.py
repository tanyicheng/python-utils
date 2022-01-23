import fire


class Building(object):

    def __init__(self, name, stories=1):
        self.name = name
        self.stories = 1

    def climb_stairs(self, stairs_per_story=10):
        for story in range(self.stories):
            for stair in range(1, stairs_per_story):
                yield stair
                yield 'Phew!'
        yield 'Done!'
        print(self.name)


if __name__ == '__main__':
    fire.Fire(Building)

# >test02.py --name="shang hai" --stories=3 climb_stairs 10
