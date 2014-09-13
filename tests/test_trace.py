#!/usr/bin/env python3
import unittest
import os
from glob import glob
import sys
sys.path.append('.')

from .utils import compare_paths, red
import yap
from tests import tracer


class A(object):
    def m(self, x):
        return x

def main(a):
    a.m(12)


class Test(unittest.TestCase):

    regtests_dir = 'regtests'
    regtests_path = os.path.join(regtests_dir, '*.yp')

    @unittest.skip
    def test_trace_trace(self):
        a = A()
        db = tracer.trace(main, [a])
        dbs = tracer.format_db(db)
        print(dbs)

    def test_trace(self):
        yps = glob(self.regtests_path)
        self.assertTrue(yps)
        for yp in yps:
            print('Tracing compilation of {}'.format(yp))
            db = tracer.trace(yap.main, [[
                '-o', '/dev/null', yp,
            ]])
            dbs = tracer.format_db(db)

            ref_path = '{}.yml'.format(yp)
            test_path = '{}-test.yml'.format(yp)

            with open(test_path, 'w') as f:
                f.write(dbs)
            #with open(ref_path) as f:
            #    dbs_ref = f.read()

            errors = compare_paths(ref_path, test_path, 'Trace')
            if errors:
                raise AssertionError(red(
                    'There have been {} errors with {}.'.format(errors, yp)))
            else:
                # Clean up only on success
                os.remove(test_path)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    unittest.TextTestRunner(verbosity=2).run(suite)
