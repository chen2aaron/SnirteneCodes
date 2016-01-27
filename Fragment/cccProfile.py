import cProfile
import pstats
import StringIO


def profiler(func):
    def wrapper(*args, **kwargs):
        datafn = func.__name__ + ".profile"  # Name the data file
        prof = cProfile.Profile()
        retval = prof.runcall(func, *args, **kwargs)
        # prof.dump_stats(datafn)
        s = StringIO.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(prof, stream=s).sort_stats(sortby)
        ps.print_stats()
        print s.getvalue()
        return retval

    return wrapper
