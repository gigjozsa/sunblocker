# sunblocker
A (python pyrap) method to remove solar-like RFI from interferometric data

Copyright (c) 2017 Gyula Istvan Geza Jozsa, Paolo Serra, Kshitij Thorat, Sphesihle Makhatini, NRF (Square Kilometre Array South Africa) - All Rights Reserved
The source may be distributed, modified, and used within the current research units and research groups of the authors or with expressive permission by the authors.
For requesting permission of usage and distribution, please write to: jozsa@ska.ac.za

Usage:
Use method phazer of class Sunblocker in module sunblocker. See description therein. E.g.:

...
import sunblocker
mysb = sunblocker.Sunblocker()
mysb.phazer(['yoyo.ms'], outset = ['yoyout.ms'], channels = a, imsize = 512, cell = 4, pol = 'i', threshold = 4., mode = 'all', radrange = 0, angle = 0, show = 'test.pdf', verb = True, dryrun = False)
...


