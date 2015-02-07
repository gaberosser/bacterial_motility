__author__ = 'gabriel'
import numpy as np
import csv


class Track(object):

    def __init__(self, data):
        """
        :param data: 2 x N array containing track coordinates
        :return:
        """
        self.data = np.array(data)
        assert self.data.shape[0] == 2, "Data must be in the form of a 2 x N matrix"

    def __len__(self):
        return self.data.shape[1]


class TrackCollection(object):

    @staticmethod
    def from_txt(infile):
        with open(infile, 'r') as f:
            reader = csv.reader(f)
            tracks = []
            for row in reader:
                this_track = [
                    [float(col) for col in row],
                    [float(col) for col in reader.next()]
                ]
                tracks.append(Track(this_track))

            return TrackCollection(tracks)

    def __init__(self, tracks):
        """

        :param tracks: Iterable containing track objects
        :return:
        """
        self.tracks = tracks
        for t in tracks:
            assert isinstance(t, Track), "Must supply an iterable of Track instances"

    def __len__(self):
        return len(self.tracks)