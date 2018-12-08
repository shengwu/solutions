from collections import Counter, defaultdict
import datetime

inp = '''
[1518-09-14 00:54] wakes up
[1518-04-15 23:58] Guard #373 begins shift
[1518-07-25 00:53] wakes up
[1518-07-04 00:45] wakes up
[1518-07-26 00:51] wakes up
[1518-06-21 00:43] falls asleep
[1518-04-24 00:57] falls asleep
[1518-11-20 00:52] wakes up
[1518-04-20 00:39] falls asleep
[1518-05-31 00:48] wakes up
[1518-09-03 00:16] falls asleep
[1518-03-26 23:50] Guard #173 begins shift
[1518-03-14 00:34] falls asleep
[1518-04-09 00:20] wakes up
[1518-09-05 00:40] falls asleep
[1518-06-12 23:59] Guard #2339 begins shift
[1518-05-09 23:46] Guard #373 begins shift
[1518-08-08 00:59] wakes up
[1518-06-06 00:08] falls asleep
[1518-09-10 00:58] wakes up
[1518-10-08 00:02] Guard #751 begins shift
[1518-04-23 00:49] wakes up
[1518-10-13 23:59] Guard #2339 begins shift
[1518-10-14 00:28] falls asleep
[1518-06-27 00:21] falls asleep
[1518-04-11 00:49] wakes up
[1518-02-06 00:46] falls asleep
[1518-08-16 00:14] wakes up
[1518-11-19 00:34] falls asleep
[1518-03-05 00:12] falls asleep
[1518-05-24 23:57] Guard #523 begins shift
[1518-06-22 00:42] wakes up
[1518-02-14 23:57] Guard #3229 begins shift
[1518-09-10 00:48] falls asleep
[1518-10-24 00:09] falls asleep
[1518-04-23 00:45] falls asleep
[1518-07-05 00:30] falls asleep
[1518-05-10 00:54] wakes up
[1518-10-24 00:57] wakes up
[1518-02-09 00:04] Guard #173 begins shift
[1518-05-29 00:51] falls asleep
[1518-02-14 00:41] falls asleep
[1518-04-08 00:40] wakes up
[1518-09-06 00:33] wakes up
[1518-02-07 23:57] Guard #2339 begins shift
[1518-05-20 00:42] falls asleep
[1518-10-03 00:01] falls asleep
[1518-10-28 00:03] Guard #1031 begins shift
[1518-02-18 00:37] wakes up
[1518-01-16 00:55] wakes up
[1518-08-03 00:04] Guard #373 begins shift
[1518-08-28 23:48] Guard #2857 begins shift
[1518-03-12 00:00] Guard #431 begins shift
[1518-05-20 00:32] wakes up
[1518-05-24 00:42] falls asleep
[1518-01-29 00:54] wakes up
[1518-07-20 00:24] wakes up
[1518-06-20 00:04] Guard #173 begins shift
[1518-08-05 00:51] wakes up
[1518-10-29 00:34] falls asleep
[1518-10-13 00:12] falls asleep
[1518-01-24 00:58] wakes up
[1518-02-21 23:49] Guard #419 begins shift
[1518-10-22 00:49] wakes up
[1518-06-15 23:52] Guard #1627 begins shift
[1518-06-11 00:57] wakes up
[1518-02-28 00:25] wakes up
[1518-03-01 00:36] wakes up
[1518-08-02 00:10] falls asleep
[1518-10-14 00:54] wakes up
[1518-08-29 23:59] Guard #3229 begins shift
[1518-11-15 00:19] wakes up
[1518-09-24 00:30] wakes up
[1518-11-01 23:59] Guard #1031 begins shift
[1518-06-18 00:13] falls asleep
[1518-06-25 00:59] wakes up
[1518-04-09 00:01] falls asleep
[1518-05-22 00:02] Guard #2857 begins shift
[1518-05-13 00:57] wakes up
[1518-06-15 00:41] falls asleep
[1518-02-25 00:53] wakes up
[1518-10-26 00:32] wakes up
[1518-06-08 00:12] falls asleep
[1518-03-06 00:34] wakes up
[1518-04-04 00:38] falls asleep
[1518-05-29 00:09] falls asleep
[1518-10-02 23:48] Guard #431 begins shift
[1518-04-10 00:49] falls asleep
[1518-05-06 00:16] falls asleep
[1518-10-10 00:00] falls asleep
[1518-01-20 00:57] wakes up
[1518-08-10 00:03] Guard #419 begins shift
[1518-02-05 00:58] wakes up
[1518-04-30 00:44] wakes up
[1518-08-10 00:11] falls asleep
[1518-05-16 00:00] Guard #863 begins shift
[1518-11-23 00:42] wakes up
[1518-09-11 00:34] falls asleep
[1518-07-22 00:03] Guard #2857 begins shift
[1518-04-15 00:36] wakes up
[1518-06-09 23:57] Guard #3209 begins shift
[1518-07-02 00:39] wakes up
[1518-01-15 00:50] wakes up
[1518-11-08 00:51] wakes up
[1518-04-16 00:44] wakes up
[1518-05-19 23:56] Guard #431 begins shift
[1518-10-01 00:10] falls asleep
[1518-03-22 00:02] Guard #751 begins shift
[1518-07-12 00:58] wakes up
[1518-11-11 00:12] falls asleep
[1518-10-02 00:48] wakes up
[1518-04-05 00:24] wakes up
[1518-02-10 00:35] wakes up
[1518-07-24 00:53] wakes up
[1518-05-18 00:57] wakes up
[1518-01-20 00:21] falls asleep
[1518-06-29 00:43] wakes up
[1518-03-15 00:40] falls asleep
[1518-07-08 00:32] wakes up
[1518-05-30 00:43] wakes up
[1518-02-02 00:25] falls asleep
[1518-02-05 00:25] falls asleep
[1518-05-11 00:31] falls asleep
[1518-02-22 00:59] wakes up
[1518-08-16 00:31] falls asleep
[1518-02-10 00:58] wakes up
[1518-07-11 00:56] wakes up
[1518-09-01 00:55] falls asleep
[1518-09-16 00:36] falls asleep
[1518-10-04 00:17] falls asleep
[1518-04-06 23:57] Guard #2857 begins shift
[1518-11-19 00:01] falls asleep
[1518-11-16 00:32] wakes up
[1518-10-08 00:30] falls asleep
[1518-02-10 00:06] falls asleep
[1518-07-08 00:36] falls asleep
[1518-04-19 00:00] Guard #3229 begins shift
[1518-08-19 00:52] wakes up
[1518-07-21 00:57] wakes up
[1518-05-12 00:00] Guard #3187 begins shift
[1518-05-23 00:47] wakes up
[1518-11-02 00:46] wakes up
[1518-11-04 00:24] falls asleep
[1518-10-20 00:21] falls asleep
[1518-05-19 00:54] wakes up
[1518-07-07 00:00] Guard #1637 begins shift
[1518-10-08 00:56] wakes up
[1518-08-12 00:52] wakes up
[1518-08-03 00:28] falls asleep
[1518-04-01 00:03] Guard #1627 begins shift
[1518-08-26 00:30] falls asleep
[1518-04-26 00:43] wakes up
[1518-05-27 00:51] falls asleep
[1518-04-10 23:56] Guard #2143 begins shift
[1518-02-15 00:14] falls asleep
[1518-06-02 00:52] wakes up
[1518-05-28 00:29] falls asleep
[1518-10-12 00:00] Guard #2143 begins shift
[1518-11-21 23:58] Guard #2339 begins shift
[1518-10-25 00:32] falls asleep
[1518-09-05 00:00] Guard #3229 begins shift
[1518-10-08 00:47] falls asleep
[1518-03-09 00:40] falls asleep
[1518-04-26 00:35] wakes up
[1518-05-17 00:02] Guard #173 begins shift
[1518-08-13 23:59] Guard #431 begins shift
[1518-10-23 00:38] falls asleep
[1518-03-20 00:49] falls asleep
[1518-06-17 00:38] falls asleep
[1518-03-31 00:57] wakes up
[1518-04-01 00:57] wakes up
[1518-08-31 00:45] falls asleep
[1518-04-04 00:15] wakes up
[1518-04-18 00:48] falls asleep
[1518-03-10 00:13] falls asleep
[1518-04-26 00:41] falls asleep
[1518-10-04 00:02] Guard #521 begins shift
[1518-09-16 00:00] Guard #863 begins shift
[1518-07-03 00:58] wakes up
[1518-05-22 00:49] wakes up
[1518-04-15 00:49] falls asleep
[1518-05-08 00:23] falls asleep
[1518-10-15 23:59] Guard #863 begins shift
[1518-07-18 00:20] wakes up
[1518-05-23 00:27] falls asleep
[1518-06-03 00:38] falls asleep
[1518-11-15 00:06] falls asleep
[1518-03-12 00:50] wakes up
[1518-11-23 00:56] wakes up
[1518-03-02 00:29] falls asleep
[1518-03-07 00:33] falls asleep
[1518-02-28 00:46] wakes up
[1518-06-16 00:37] falls asleep
[1518-07-28 23:58] Guard #1597 begins shift
[1518-05-21 00:52] wakes up
[1518-09-30 00:55] wakes up
[1518-04-16 00:57] wakes up
[1518-08-02 00:22] wakes up
[1518-06-28 00:00] falls asleep
[1518-05-08 00:11] wakes up
[1518-04-02 00:02] falls asleep
[1518-01-17 23:51] Guard #3187 begins shift
[1518-03-01 00:59] wakes up
[1518-01-26 00:51] falls asleep
[1518-09-27 00:23] falls asleep
[1518-09-09 00:31] falls asleep
[1518-02-02 00:56] wakes up
[1518-03-09 00:55] falls asleep
[1518-02-13 00:02] Guard #2143 begins shift
[1518-08-09 00:43] wakes up
[1518-04-29 00:29] falls asleep
[1518-09-25 00:14] falls asleep
[1518-02-08 00:29] falls asleep
[1518-04-19 00:40] wakes up
[1518-10-25 00:59] wakes up
[1518-06-26 00:13] falls asleep
[1518-08-14 23:59] Guard #521 begins shift
[1518-03-04 00:54] falls asleep
[1518-10-17 00:52] wakes up
[1518-08-23 00:30] wakes up
[1518-08-13 00:07] falls asleep
[1518-02-05 23:56] Guard #1627 begins shift
[1518-06-19 00:02] Guard #173 begins shift
[1518-07-05 00:48] wakes up
[1518-10-26 00:47] wakes up
[1518-04-20 00:55] wakes up
[1518-10-25 00:50] wakes up
[1518-07-02 00:12] falls asleep
[1518-02-14 00:02] Guard #2539 begins shift
[1518-02-21 00:34] wakes up
[1518-10-14 23:59] Guard #3209 begins shift
[1518-03-27 00:27] falls asleep
[1518-08-17 00:13] falls asleep
[1518-07-31 00:00] falls asleep
[1518-05-30 00:35] falls asleep
[1518-10-04 00:55] wakes up
[1518-07-18 00:56] wakes up
[1518-07-19 23:50] Guard #3209 begins shift
[1518-03-16 00:39] wakes up
[1518-07-18 00:49] falls asleep
[1518-09-20 00:16] falls asleep
[1518-03-19 00:50] wakes up
[1518-10-29 00:03] Guard #419 begins shift
[1518-08-09 00:06] falls asleep
[1518-04-24 00:58] wakes up
[1518-06-01 00:24] wakes up
[1518-04-05 00:19] falls asleep
[1518-02-17 00:53] wakes up
[1518-11-17 23:57] Guard #1597 begins shift
[1518-03-07 00:50] wakes up
[1518-06-26 00:00] Guard #3187 begins shift
[1518-10-16 00:51] falls asleep
[1518-07-09 00:55] wakes up
[1518-09-05 00:36] wakes up
[1518-09-21 23:57] Guard #173 begins shift
[1518-06-30 23:48] Guard #2143 begins shift
[1518-03-24 00:15] wakes up
[1518-04-17 23:59] Guard #2339 begins shift
[1518-09-11 00:04] Guard #2143 begins shift
[1518-04-08 23:50] Guard #173 begins shift
[1518-01-23 00:07] falls asleep
[1518-04-01 00:48] wakes up
[1518-08-11 00:44] wakes up
[1518-01-26 00:20] falls asleep
[1518-07-13 00:02] falls asleep
[1518-04-14 00:02] falls asleep
[1518-11-12 00:44] wakes up
[1518-06-06 00:35] falls asleep
[1518-03-28 00:00] Guard #419 begins shift
[1518-09-29 23:56] Guard #1597 begins shift
[1518-09-09 00:25] wakes up
[1518-07-11 00:01] Guard #2339 begins shift
[1518-09-10 00:43] wakes up
[1518-08-07 00:28] falls asleep
[1518-10-23 00:35] wakes up
[1518-10-31 00:04] Guard #3187 begins shift
[1518-08-18 00:44] falls asleep
[1518-03-25 00:48] falls asleep
[1518-08-03 00:47] wakes up
[1518-06-20 00:34] falls asleep
[1518-03-13 00:01] falls asleep
[1518-06-10 00:27] wakes up
[1518-05-26 00:31] falls asleep
[1518-11-10 00:58] wakes up
[1518-07-01 00:58] wakes up
[1518-08-11 00:57] wakes up
[1518-10-16 00:46] falls asleep
[1518-03-14 00:36] wakes up
[1518-09-27 23:56] Guard #3187 begins shift
[1518-06-30 00:46] falls asleep
[1518-03-10 00:02] Guard #863 begins shift
[1518-04-04 00:03] Guard #523 begins shift
[1518-09-14 00:01] Guard #3229 begins shift
[1518-02-08 00:17] falls asleep
[1518-03-23 00:39] falls asleep
[1518-09-28 00:19] falls asleep
[1518-10-04 23:56] Guard #521 begins shift
[1518-02-16 00:57] wakes up
[1518-04-27 23:59] Guard #373 begins shift
[1518-02-19 00:31] falls asleep
[1518-11-23 00:10] falls asleep
[1518-04-08 00:04] Guard #2339 begins shift
[1518-06-01 00:02] Guard #1031 begins shift
[1518-09-19 00:23] falls asleep
[1518-07-14 00:30] wakes up
[1518-11-01 00:45] wakes up
[1518-03-26 00:27] falls asleep
[1518-04-23 00:02] Guard #521 begins shift
[1518-04-28 00:26] falls asleep
[1518-03-07 00:27] wakes up
[1518-09-23 00:57] wakes up
[1518-04-01 00:12] falls asleep
[1518-11-11 00:01] Guard #3209 begins shift
[1518-08-08 00:09] falls asleep
[1518-11-09 00:04] Guard #523 begins shift
[1518-11-19 00:58] wakes up
[1518-03-16 00:03] falls asleep
[1518-04-22 00:04] falls asleep
[1518-10-11 00:00] Guard #2143 begins shift
[1518-09-27 00:52] wakes up
[1518-05-07 00:00] falls asleep
[1518-02-11 00:53] wakes up
[1518-09-24 00:57] wakes up
[1518-08-24 00:52] wakes up
[1518-09-04 00:18] falls asleep
[1518-07-14 00:28] falls asleep
[1518-09-15 00:25] falls asleep
[1518-11-23 00:01] Guard #2857 begins shift
[1518-08-08 00:46] falls asleep
[1518-08-04 00:58] wakes up
[1518-02-22 00:01] falls asleep
[1518-03-25 00:36] wakes up
[1518-03-02 00:55] wakes up
[1518-09-23 23:46] Guard #2143 begins shift
[1518-08-28 00:35] falls asleep
[1518-04-15 00:06] falls asleep
[1518-07-24 00:32] wakes up
[1518-07-12 00:57] falls asleep
[1518-11-04 00:00] Guard #3229 begins shift
[1518-02-08 00:23] wakes up
[1518-04-12 00:46] wakes up
[1518-09-04 00:54] wakes up
[1518-02-21 00:11] falls asleep
[1518-10-30 00:02] Guard #2339 begins shift
[1518-07-04 00:35] falls asleep
[1518-04-15 00:00] Guard #1597 begins shift
[1518-08-18 00:23] falls asleep
[1518-07-29 00:51] wakes up
[1518-06-06 00:21] wakes up
[1518-06-17 00:41] wakes up
[1518-04-19 00:28] falls asleep
[1518-02-10 00:47] wakes up
[1518-08-28 00:32] wakes up
[1518-03-15 00:27] falls asleep
[1518-05-11 00:00] Guard #1031 begins shift
[1518-08-04 00:11] falls asleep
[1518-05-03 00:02] Guard #3209 begins shift
[1518-07-20 00:39] falls asleep
[1518-05-09 00:52] wakes up
[1518-06-29 00:23] wakes up
[1518-05-26 23:47] Guard #863 begins shift
[1518-07-28 00:58] wakes up
[1518-11-10 00:24] wakes up
[1518-06-24 23:57] Guard #863 begins shift
[1518-03-23 00:04] falls asleep
[1518-03-06 00:49] falls asleep
[1518-10-14 00:49] wakes up
[1518-07-04 00:36] wakes up
[1518-02-05 00:33] falls asleep
[1518-01-22 00:01] Guard #2339 begins shift
[1518-11-14 00:48] wakes up
[1518-05-17 00:57] wakes up
[1518-08-23 00:18] falls asleep
[1518-11-12 00:14] falls asleep
[1518-03-18 00:44] wakes up
[1518-04-14 00:17] wakes up
[1518-06-04 00:58] wakes up
[1518-11-07 00:55] wakes up
[1518-05-19 00:23] falls asleep
[1518-02-13 00:47] falls asleep
[1518-09-18 23:59] Guard #419 begins shift
[1518-09-25 23:56] Guard #419 begins shift
[1518-07-19 00:18] falls asleep
[1518-03-24 23:48] Guard #1597 begins shift
[1518-08-21 00:18] falls asleep
[1518-07-27 00:44] wakes up
[1518-11-04 00:36] wakes up
[1518-01-13 23:56] Guard #751 begins shift
[1518-01-18 00:32] wakes up
[1518-09-17 23:57] Guard #521 begins shift
[1518-11-03 00:47] wakes up
[1518-10-09 00:58] wakes up
[1518-07-15 00:01] Guard #419 begins shift
[1518-09-17 00:10] falls asleep
[1518-06-24 00:20] falls asleep
[1518-03-23 00:36] wakes up
[1518-01-30 00:55] wakes up
[1518-01-26 00:45] wakes up
[1518-02-03 00:33] wakes up
[1518-02-02 23:47] Guard #3229 begins shift
[1518-11-05 23:56] Guard #523 begins shift
[1518-06-26 00:22] wakes up
[1518-01-28 00:56] wakes up
[1518-05-27 00:05] falls asleep
[1518-11-16 00:14] falls asleep
[1518-08-24 00:22] wakes up
[1518-07-16 00:57] wakes up
[1518-04-10 00:54] wakes up
[1518-03-13 00:43] wakes up
[1518-09-08 00:00] Guard #173 begins shift
[1518-09-26 00:45] wakes up
[1518-07-27 00:18] falls asleep
[1518-07-22 00:59] wakes up
[1518-06-11 00:04] Guard #2339 begins shift
[1518-07-05 00:01] Guard #173 begins shift
[1518-03-12 00:33] wakes up
[1518-04-03 00:20] falls asleep
[1518-11-05 00:42] falls asleep
[1518-11-22 00:22] falls asleep
[1518-06-26 00:41] wakes up
[1518-07-01 00:34] wakes up
[1518-08-08 23:57] Guard #3209 begins shift
[1518-10-07 00:22] wakes up
[1518-04-17 00:43] falls asleep
[1518-08-02 00:36] falls asleep
[1518-06-05 00:46] falls asleep
[1518-03-06 00:52] wakes up
[1518-02-10 00:53] falls asleep
[1518-05-10 00:05] falls asleep
[1518-02-18 00:47] falls asleep
[1518-05-31 00:00] Guard #3187 begins shift
[1518-07-23 00:54] wakes up
[1518-08-27 00:53] wakes up
[1518-10-10 00:34] wakes up
[1518-10-09 00:02] Guard #863 begins shift
[1518-11-15 23:59] Guard #3209 begins shift
[1518-08-25 00:39] falls asleep
[1518-01-21 00:56] wakes up
[1518-06-07 23:57] Guard #3209 begins shift
[1518-08-09 00:46] falls asleep
[1518-06-06 00:01] Guard #1637 begins shift
[1518-05-18 00:26] falls asleep
[1518-06-02 23:53] Guard #431 begins shift
[1518-09-30 00:15] falls asleep
[1518-07-02 00:03] Guard #2857 begins shift
[1518-02-24 00:07] falls asleep
[1518-08-19 00:01] Guard #1637 begins shift
[1518-01-15 00:27] falls asleep
[1518-05-16 00:51] falls asleep
[1518-07-09 00:54] falls asleep
[1518-07-03 00:35] wakes up
[1518-10-20 00:31] wakes up
[1518-09-04 00:27] wakes up
[1518-10-05 23:58] Guard #1597 begins shift
[1518-02-12 00:59] wakes up
[1518-06-22 00:01] Guard #3209 begins shift
[1518-01-31 00:34] falls asleep
[1518-05-19 00:32] wakes up
[1518-01-27 00:44] wakes up
[1518-05-23 00:08] wakes up
[1518-02-27 00:18] wakes up
[1518-06-03 23:56] Guard #373 begins shift
[1518-03-22 00:11] falls asleep
[1518-04-30 00:31] falls asleep
[1518-09-09 23:59] Guard #1597 begins shift
[1518-05-26 00:01] Guard #431 begins shift
[1518-01-30 23:59] Guard #2143 begins shift
[1518-02-27 23:56] Guard #751 begins shift
[1518-07-03 00:01] Guard #373 begins shift
[1518-04-05 00:46] falls asleep
[1518-10-27 00:02] Guard #991 begins shift
[1518-10-17 00:01] Guard #3229 begins shift
[1518-08-27 00:47] falls asleep
[1518-10-12 00:43] falls asleep
[1518-09-20 00:53] wakes up
[1518-11-22 00:37] wakes up
[1518-04-04 00:08] falls asleep
[1518-09-07 00:49] wakes up
[1518-06-08 00:27] wakes up
[1518-06-30 00:03] Guard #523 begins shift
[1518-04-21 00:46] falls asleep
[1518-05-12 00:15] wakes up
[1518-07-26 00:18] falls asleep
[1518-10-15 00:15] falls asleep
[1518-02-14 00:48] wakes up
[1518-03-04 00:57] wakes up
[1518-06-21 00:54] wakes up
[1518-08-23 23:56] Guard #523 begins shift
[1518-07-26 00:00] Guard #1627 begins shift
[1518-05-24 00:44] wakes up
[1518-04-05 00:01] Guard #2539 begins shift
[1518-02-06 00:52] falls asleep
[1518-04-07 00:55] falls asleep
[1518-08-18 00:53] wakes up
[1518-09-22 00:34] falls asleep
[1518-04-25 00:01] Guard #2339 begins shift
[1518-11-21 00:54] wakes up
[1518-01-23 00:00] Guard #1627 begins shift
[1518-11-13 23:58] Guard #173 begins shift
[1518-10-11 00:41] wakes up
[1518-09-02 00:46] falls asleep
[1518-05-07 00:49] wakes up
[1518-01-24 00:00] Guard #373 begins shift
[1518-03-12 00:28] falls asleep
[1518-01-14 00:57] wakes up
[1518-04-24 00:53] wakes up
[1518-07-15 23:59] Guard #1627 begins shift
[1518-03-03 00:58] wakes up
[1518-11-04 23:58] Guard #523 begins shift
[1518-03-14 00:04] falls asleep
[1518-05-02 00:00] Guard #2339 begins shift
[1518-10-13 00:03] Guard #173 begins shift
[1518-01-30 00:09] falls asleep
[1518-09-12 00:07] falls asleep
[1518-06-29 00:21] falls asleep
[1518-02-14 00:16] falls asleep
[1518-05-25 00:36] falls asleep
[1518-08-05 00:42] falls asleep
[1518-07-10 00:44] wakes up
[1518-09-16 00:54] falls asleep
[1518-02-01 00:59] wakes up
[1518-02-28 00:32] falls asleep
[1518-09-26 23:59] Guard #373 begins shift
[1518-09-05 00:18] wakes up
[1518-03-12 23:52] Guard #373 begins shift
[1518-10-10 00:55] wakes up
[1518-09-16 00:49] wakes up
[1518-02-06 00:49] wakes up
[1518-05-02 00:38] falls asleep
[1518-03-18 00:37] falls asleep
[1518-02-24 00:56] wakes up
[1518-08-14 00:27] falls asleep
[1518-08-31 00:55] wakes up
[1518-05-29 23:57] Guard #419 begins shift
[1518-11-02 00:12] falls asleep
[1518-09-18 00:26] falls asleep
[1518-09-05 00:52] falls asleep
[1518-02-18 00:54] wakes up
[1518-05-16 00:17] falls asleep
[1518-03-03 00:40] wakes up
[1518-03-27 00:06] wakes up
[1518-05-13 00:44] falls asleep
[1518-09-12 00:30] wakes up
[1518-02-13 00:58] wakes up
[1518-08-20 00:43] falls asleep
[1518-06-10 00:08] falls asleep
[1518-07-12 23:46] Guard #373 begins shift
[1518-07-30 00:08] falls asleep
[1518-03-01 00:08] falls asleep
[1518-06-28 23:59] Guard #173 begins shift
[1518-04-21 00:37] falls asleep
[1518-03-28 00:33] falls asleep
[1518-07-13 00:55] falls asleep
[1518-08-12 00:27] falls asleep
[1518-07-05 23:48] Guard #431 begins shift
[1518-10-06 23:57] Guard #3187 begins shift
[1518-06-21 00:40] wakes up
[1518-03-28 00:48] wakes up
[1518-03-20 00:03] Guard #431 begins shift
[1518-08-02 00:00] Guard #1627 begins shift
[1518-02-11 00:50] falls asleep
[1518-03-08 00:18] falls asleep
[1518-09-09 00:59] wakes up
[1518-10-07 00:57] wakes up
[1518-10-21 00:58] wakes up
[1518-07-20 00:03] falls asleep
[1518-09-29 00:53] wakes up
[1518-02-20 00:01] Guard #601 begins shift
[1518-05-24 00:03] falls asleep
[1518-09-06 23:59] Guard #523 begins shift
[1518-06-30 00:55] wakes up
[1518-07-09 23:59] Guard #1627 begins shift
[1518-11-18 00:36] falls asleep
[1518-05-14 00:59] wakes up
[1518-02-15 23:52] Guard #173 begins shift
[1518-04-25 23:50] Guard #1637 begins shift
[1518-02-22 23:58] Guard #863 begins shift
[1518-07-27 23:46] Guard #1597 begins shift
[1518-07-01 00:00] falls asleep
[1518-01-26 00:52] wakes up
[1518-06-21 00:37] falls asleep
[1518-01-18 00:04] falls asleep
[1518-06-16 00:50] wakes up
[1518-08-20 00:53] wakes up
[1518-01-20 00:00] Guard #2339 begins shift
[1518-03-19 00:47] falls asleep
[1518-09-05 00:25] falls asleep
[1518-04-14 00:40] falls asleep
[1518-07-08 00:48] wakes up
[1518-10-31 00:51] wakes up
[1518-03-12 00:42] falls asleep
[1518-08-17 00:57] wakes up
[1518-03-31 00:21] falls asleep
[1518-04-13 00:00] falls asleep
[1518-01-17 00:17] falls asleep
[1518-11-07 00:00] falls asleep
[1518-07-24 00:00] Guard #863 begins shift
[1518-10-06 00:28] falls asleep
[1518-05-23 00:05] falls asleep
[1518-03-29 23:57] Guard #3209 begins shift
[1518-09-30 23:56] Guard #419 begins shift
[1518-01-27 00:32] falls asleep
[1518-01-13 00:21] wakes up
[1518-04-13 23:47] Guard #3187 begins shift
[1518-06-07 00:02] Guard #3187 begins shift
[1518-02-18 00:11] falls asleep
[1518-07-29 00:16] falls asleep
[1518-08-17 00:52] wakes up
[1518-10-05 00:11] falls asleep
[1518-02-05 00:38] wakes up
[1518-05-13 00:36] falls asleep
[1518-10-24 00:44] wakes up
[1518-07-25 00:00] Guard #373 begins shift
[1518-02-13 00:54] wakes up
[1518-04-05 00:57] wakes up
[1518-07-09 00:02] Guard #373 begins shift
[1518-06-23 00:45] falls asleep
[1518-03-13 23:54] Guard #1637 begins shift
[1518-11-06 23:53] Guard #1637 begins shift
[1518-02-26 23:58] Guard #419 begins shift
[1518-05-18 00:48] falls asleep
[1518-02-06 23:58] Guard #2857 begins shift
[1518-01-20 00:56] falls asleep
[1518-05-08 00:58] wakes up
[1518-10-25 00:56] falls asleep
[1518-02-01 00:01] Guard #2857 begins shift
[1518-11-08 00:01] Guard #521 begins shift
[1518-02-05 00:53] wakes up
[1518-10-08 00:42] wakes up
[1518-08-24 23:58] Guard #521 begins shift
[1518-01-24 00:29] falls asleep
[1518-03-23 23:54] Guard #523 begins shift
[1518-09-08 00:20] wakes up
[1518-10-22 00:54] falls asleep
[1518-09-18 00:54] wakes up
[1518-05-09 00:47] wakes up
[1518-09-28 00:54] falls asleep
[1518-07-12 00:51] wakes up
[1518-07-30 00:00] Guard #173 begins shift
[1518-11-20 23:50] Guard #751 begins shift
[1518-10-19 00:25] falls asleep
[1518-07-24 00:08] falls asleep
[1518-03-03 00:14] falls asleep
[1518-10-16 00:47] wakes up
[1518-10-10 00:47] falls asleep
[1518-01-12 23:57] Guard #3209 begins shift
[1518-04-06 00:01] Guard #419 begins shift
[1518-06-05 00:04] Guard #2539 begins shift
[1518-07-14 00:59] wakes up
[1518-05-26 00:45] falls asleep
[1518-09-12 00:01] Guard #1597 begins shift
[1518-08-11 00:03] Guard #3209 begins shift
[1518-10-07 00:20] falls asleep
[1518-10-28 00:35] wakes up
[1518-10-04 00:14] wakes up
[1518-03-15 23:47] Guard #431 begins shift
[1518-05-01 00:11] falls asleep
[1518-05-28 00:36] falls asleep
[1518-04-02 00:39] wakes up
[1518-10-20 23:57] Guard #1637 begins shift
[1518-10-30 00:44] wakes up
[1518-09-24 00:05] falls asleep
[1518-11-06 00:49] wakes up
[1518-10-22 00:16] falls asleep
[1518-06-23 00:57] wakes up
[1518-07-09 00:43] wakes up
[1518-02-03 00:03] falls asleep
[1518-02-01 23:57] Guard #3229 begins shift
[1518-06-04 00:40] falls asleep
[1518-09-19 00:31] wakes up
[1518-05-19 00:03] Guard #2539 begins shift
[1518-02-07 00:12] falls asleep
[1518-09-26 00:33] falls asleep
[1518-05-26 00:58] wakes up
[1518-08-29 00:38] wakes up
[1518-09-12 23:50] Guard #521 begins shift
[1518-09-15 00:34] wakes up
[1518-08-22 00:47] wakes up
[1518-03-25 00:01] falls asleep
[1518-10-04 00:45] wakes up
[1518-11-01 00:02] Guard #373 begins shift
[1518-03-30 00:56] wakes up
[1518-01-26 00:38] wakes up
[1518-03-17 00:59] wakes up
[1518-03-29 00:49] wakes up
[1518-03-26 00:41] falls asleep
[1518-01-29 00:23] falls asleep
[1518-03-11 00:41] falls asleep
[1518-04-11 23:57] Guard #2857 begins shift
[1518-09-19 00:56] falls asleep
[1518-03-22 00:46] wakes up
[1518-07-16 00:38] falls asleep
[1518-03-08 00:00] Guard #1597 begins shift
[1518-06-07 00:18] falls asleep
[1518-06-01 00:45] wakes up
[1518-09-24 23:58] Guard #1627 begins shift
[1518-05-21 00:35] falls asleep
[1518-01-28 00:50] falls asleep
[1518-01-25 00:19] falls asleep
[1518-10-16 00:59] wakes up
[1518-03-02 00:00] Guard #1031 begins shift
[1518-07-30 00:35] wakes up
[1518-11-13 00:04] Guard #419 begins shift
[1518-03-09 00:52] wakes up
[1518-06-12 00:59] wakes up
[1518-03-15 00:00] Guard #2339 begins shift
[1518-09-06 00:00] Guard #1637 begins shift
[1518-03-10 23:50] Guard #863 begins shift
[1518-02-15 00:36] wakes up
[1518-04-21 00:59] wakes up
[1518-03-11 00:33] wakes up
[1518-09-23 00:14] falls asleep
[1518-09-09 00:49] wakes up
[1518-10-13 00:32] wakes up
[1518-10-14 00:52] falls asleep
[1518-02-12 00:51] falls asleep
[1518-08-05 00:02] Guard #751 begins shift
[1518-09-03 00:52] wakes up
[1518-04-12 00:55] wakes up
[1518-06-15 00:20] wakes up
[1518-08-07 23:56] Guard #3229 begins shift
[1518-04-30 00:55] falls asleep
[1518-04-02 00:36] falls asleep
[1518-05-16 00:52] wakes up
[1518-09-25 00:55] wakes up
[1518-03-29 00:00] Guard #431 begins shift
[1518-02-18 00:00] Guard #373 begins shift
[1518-10-03 00:45] falls asleep
[1518-05-25 00:19] falls asleep
[1518-10-21 00:44] falls asleep
[1518-11-18 00:58] wakes up
[1518-09-20 00:00] Guard #3209 begins shift
[1518-11-20 00:00] Guard #1627 begins shift
[1518-09-16 00:59] wakes up
[1518-05-04 00:29] falls asleep
[1518-04-18 00:41] wakes up
[1518-06-17 00:08] falls asleep
[1518-09-22 00:40] wakes up
[1518-10-23 23:58] Guard #1627 begins shift
[1518-01-21 00:54] falls asleep
[1518-02-09 23:58] Guard #3229 begins shift
[1518-01-17 00:03] Guard #523 begins shift
[1518-04-16 00:39] falls asleep
[1518-09-09 00:54] falls asleep
[1518-09-08 00:56] wakes up
[1518-06-07 00:19] wakes up
[1518-06-22 00:06] falls asleep
[1518-02-24 00:47] wakes up
[1518-03-19 00:58] wakes up
[1518-06-14 23:57] Guard #1637 begins shift
[1518-07-30 23:46] Guard #2857 begins shift
[1518-08-10 00:49] falls asleep
[1518-08-22 00:51] falls asleep
[1518-03-24 00:58] wakes up
[1518-04-29 00:50] wakes up
[1518-09-13 00:51] wakes up
[1518-05-24 00:33] wakes up
[1518-04-30 23:58] Guard #2539 begins shift
[1518-04-09 00:24] falls asleep
[1518-06-19 00:06] falls asleep
[1518-04-12 00:38] falls asleep
[1518-04-24 00:03] Guard #751 begins shift
[1518-07-06 00:00] falls asleep
[1518-10-03 00:30] falls asleep
[1518-07-22 23:58] Guard #1031 begins shift
[1518-08-31 23:56] Guard #3187 begins shift
[1518-04-14 00:58] wakes up
[1518-03-16 23:57] Guard #863 begins shift
[1518-04-13 00:45] wakes up
[1518-06-23 23:58] Guard #3229 begins shift
[1518-01-28 00:43] falls asleep
[1518-03-04 00:27] wakes up
[1518-04-06 00:23] falls asleep
[1518-05-25 00:22] wakes up
[1518-06-09 00:30] wakes up
[1518-02-06 00:19] wakes up
[1518-06-16 00:00] falls asleep
[1518-01-30 00:04] Guard #3187 begins shift
[1518-09-08 00:32] falls asleep
[1518-09-06 00:08] falls asleep
[1518-03-05 00:57] wakes up
[1518-07-04 00:42] falls asleep
[1518-09-17 00:52] wakes up
[1518-06-12 00:40] falls asleep
[1518-03-19 00:03] Guard #1637 begins shift
[1518-08-28 00:58] wakes up
[1518-07-20 00:46] wakes up
[1518-08-24 00:51] falls asleep
[1518-02-22 00:53] falls asleep
[1518-10-22 00:57] wakes up
[1518-05-11 00:56] wakes up
[1518-05-15 00:18] falls asleep
[1518-02-06 00:07] falls asleep
[1518-04-30 00:58] wakes up
[1518-09-02 00:50] wakes up
[1518-11-19 00:24] wakes up
[1518-08-11 00:53] falls asleep
[1518-07-08 00:04] Guard #173 begins shift
[1518-08-22 00:53] wakes up
[1518-11-09 23:58] Guard #2143 begins shift
[1518-08-24 00:13] falls asleep
[1518-03-22 23:51] Guard #601 begins shift
[1518-08-26 23:59] Guard #3187 begins shift
[1518-02-27 00:16] falls asleep
[1518-08-08 00:42] wakes up
[1518-02-06 00:58] wakes up
[1518-05-07 23:58] Guard #173 begins shift
[1518-01-26 00:43] falls asleep
[1518-03-15 00:50] wakes up
[1518-11-13 00:49] wakes up
[1518-04-30 00:04] Guard #1031 begins shift
[1518-07-01 00:54] falls asleep
[1518-08-09 00:32] falls asleep
[1518-09-19 00:34] falls asleep
[1518-01-27 00:00] Guard #3229 begins shift
[1518-04-16 00:47] falls asleep
[1518-05-14 00:03] falls asleep
[1518-06-20 00:37] wakes up
[1518-03-06 00:27] falls asleep
[1518-04-27 00:08] falls asleep
[1518-05-09 00:50] falls asleep
[1518-10-07 00:34] falls asleep
[1518-04-10 00:12] falls asleep
[1518-04-27 00:04] Guard #601 begins shift
[1518-08-02 00:55] wakes up
[1518-08-22 00:24] falls asleep
[1518-02-23 00:57] wakes up
[1518-10-29 00:41] wakes up
[1518-06-03 00:44] wakes up
[1518-08-20 23:56] Guard #1637 begins shift
[1518-11-02 00:39] falls asleep
[1518-01-16 00:37] falls asleep
[1518-02-22 00:45] wakes up
[1518-11-05 00:49] wakes up
[1518-03-25 00:57] wakes up
[1518-11-14 00:25] falls asleep
[1518-06-21 00:00] Guard #3209 begins shift
[1518-01-24 23:56] Guard #863 begins shift
[1518-03-04 00:14] falls asleep
[1518-06-03 00:35] wakes up
[1518-07-19 00:58] wakes up
[1518-09-08 00:09] falls asleep
[1518-10-03 00:26] wakes up
[1518-09-07 00:47] falls asleep
[1518-05-14 23:58] Guard #1597 begins shift
[1518-06-18 00:46] wakes up
[1518-10-23 00:24] falls asleep
[1518-04-15 00:59] wakes up
[1518-07-03 23:57] Guard #2143 begins shift
[1518-06-09 00:54] wakes up
[1518-06-11 00:42] falls asleep
[1518-09-29 00:18] falls asleep
[1518-11-06 00:08] falls asleep
[1518-07-13 00:47] wakes up
[1518-08-13 00:36] wakes up
[1518-08-20 00:02] Guard #1627 begins shift
[1518-03-27 00:39] wakes up
[1518-07-03 00:46] falls asleep
[1518-02-11 23:47] Guard #521 begins shift
[1518-04-20 00:05] falls asleep
[1518-05-24 00:47] falls asleep
[1518-11-12 00:00] Guard #2143 begins shift
[1518-06-02 00:01] falls asleep
[1518-06-25 00:31] falls asleep
[1518-06-27 23:50] Guard #3209 begins shift
[1518-08-18 00:38] wakes up
[1518-10-05 00:43] wakes up
[1518-11-04 00:45] falls asleep
[1518-04-29 00:01] Guard #523 begins shift
[1518-05-17 00:40] falls asleep
[1518-10-21 00:51] wakes up
[1518-10-26 00:41] falls asleep
[1518-02-14 00:35] wakes up
[1518-09-16 23:57] Guard #601 begins shift
[1518-08-25 23:58] Guard #2143 begins shift
[1518-11-18 23:50] Guard #523 begins shift
[1518-09-21 00:04] Guard #991 begins shift
[1518-11-01 00:11] falls asleep
[1518-08-25 00:21] wakes up
[1518-01-29 00:01] Guard #1031 begins shift
[1518-08-12 00:00] Guard #863 begins shift
[1518-07-13 00:59] wakes up
[1518-07-31 00:47] wakes up
[1518-06-01 23:54] Guard #3187 begins shift
[1518-03-26 00:01] Guard #3229 begins shift
[1518-07-24 00:38] falls asleep
[1518-06-15 00:52] wakes up
[1518-05-24 00:59] wakes up
[1518-09-05 00:10] falls asleep
[1518-09-04 00:04] Guard #1031 begins shift
[1518-08-18 00:51] falls asleep
[1518-05-28 00:04] Guard #1627 begins shift
[1518-08-11 00:20] falls asleep
[1518-10-23 00:03] Guard #2339 begins shift
[1518-04-18 00:51] wakes up
[1518-02-19 00:03] Guard #521 begins shift
[1518-03-29 00:31] falls asleep
[1518-02-20 00:13] falls asleep
[1518-11-23 00:55] falls asleep
[1518-01-28 00:44] wakes up
[1518-07-15 00:46] wakes up
[1518-04-20 23:58] Guard #373 begins shift
[1518-03-11 00:03] falls asleep
[1518-06-24 00:51] wakes up
[1518-06-29 00:32] falls asleep
[1518-08-30 00:56] wakes up
[1518-03-20 00:34] falls asleep
[1518-04-10 00:04] Guard #1031 begins shift
[1518-04-24 00:49] falls asleep
[1518-03-03 00:53] falls asleep
[1518-05-08 00:06] falls asleep
[1518-11-21 00:02] falls asleep
[1518-06-07 00:59] wakes up
[1518-10-07 00:45] wakes up
[1518-02-01 00:19] falls asleep
[1518-02-19 00:58] wakes up
[1518-05-27 00:36] wakes up
[1518-07-03 00:38] falls asleep
[1518-05-19 00:41] wakes up
[1518-08-07 00:34] wakes up
[1518-05-07 00:24] wakes up
[1518-02-25 00:19] falls asleep
[1518-09-02 00:00] Guard #521 begins shift
[1518-07-08 00:58] wakes up
[1518-11-17 00:02] Guard #1999 begins shift
[1518-10-26 00:27] falls asleep
[1518-05-02 00:54] wakes up
[1518-09-20 00:24] wakes up
[1518-03-17 00:21] falls asleep
[1518-09-10 00:36] falls asleep
[1518-10-17 00:09] falls asleep
[1518-06-05 00:57] wakes up
[1518-06-11 23:56] Guard #373 begins shift
[1518-11-13 00:37] falls asleep
[1518-08-16 00:46] wakes up
[1518-02-13 00:57] falls asleep
[1518-06-14 00:59] wakes up
[1518-05-20 00:24] falls asleep
[1518-09-29 00:00] Guard #2339 begins shift
[1518-02-06 00:22] falls asleep
[1518-11-02 23:56] Guard #1637 begins shift
[1518-08-29 00:05] falls asleep
[1518-04-11 00:26] falls asleep
[1518-10-04 00:07] falls asleep
[1518-08-10 00:31] wakes up
[1518-03-23 00:47] wakes up
[1518-05-29 00:57] wakes up
[1518-08-25 00:51] wakes up
[1518-09-26 00:48] falls asleep
[1518-05-03 00:58] wakes up
[1518-05-06 23:46] Guard #373 begins shift
[1518-11-08 00:13] falls asleep
[1518-07-14 00:00] Guard #431 begins shift
[1518-07-03 00:11] falls asleep
[1518-04-21 00:42] wakes up
[1518-09-14 23:58] Guard #3209 begins shift
[1518-06-09 00:00] Guard #431 begins shift
[1518-03-11 00:52] wakes up
[1518-07-10 00:23] falls asleep
[1518-07-14 00:40] falls asleep
[1518-06-06 00:51] wakes up
[1518-07-19 00:03] Guard #863 begins shift
[1518-01-23 00:54] wakes up
[1518-07-23 00:26] falls asleep
[1518-08-26 00:45] wakes up
[1518-07-22 00:17] falls asleep
[1518-09-26 00:57] wakes up
[1518-05-18 00:37] wakes up
[1518-10-09 00:49] falls asleep
[1518-02-08 00:47] wakes up
[1518-09-14 00:25] falls asleep
[1518-08-31 00:41] wakes up
[1518-01-25 00:51] wakes up
[1518-07-28 00:01] falls asleep
[1518-10-28 00:16] falls asleep
[1518-02-17 00:01] Guard #2857 begins shift
[1518-06-26 23:59] Guard #523 begins shift
[1518-03-06 00:44] wakes up
[1518-08-18 00:48] wakes up
[1518-07-18 00:46] wakes up
[1518-08-06 00:01] falls asleep
[1518-05-09 00:02] Guard #521 begins shift
[1518-10-09 23:50] Guard #523 begins shift
[1518-02-28 00:18] falls asleep
[1518-05-29 00:00] Guard #3187 begins shift
[1518-10-24 00:50] falls asleep
[1518-07-06 00:44] wakes up
[1518-08-28 00:31] falls asleep
[1518-01-17 00:48] wakes up
[1518-10-02 00:29] falls asleep
[1518-07-02 00:27] falls asleep
[1518-11-09 00:38] falls asleep
[1518-06-12 00:57] falls asleep
[1518-04-26 00:20] wakes up
[1518-05-10 00:14] wakes up
[1518-08-13 00:04] Guard #2857 begins shift
[1518-04-25 00:53] wakes up
[1518-03-15 00:33] wakes up
[1518-04-03 00:30] wakes up
[1518-08-21 23:58] Guard #3187 begins shift
[1518-01-18 23:58] Guard #1999 begins shift
[1518-06-22 23:56] Guard #3187 begins shift
[1518-10-06 00:59] wakes up
[1518-10-21 23:57] Guard #863 begins shift
[1518-08-28 00:00] Guard #1637 begins shift
[1518-02-11 00:44] wakes up
[1518-07-07 00:16] falls asleep
[1518-10-15 00:43] wakes up
[1518-09-05 00:56] wakes up
[1518-01-22 00:12] falls asleep
[1518-01-14 23:57] Guard #2857 begins shift
[1518-08-30 00:36] falls asleep
[1518-08-07 00:01] Guard #1597 begins shift
[1518-05-05 00:00] Guard #3229 begins shift
[1518-01-13 00:13] falls asleep
[1518-11-10 00:55] falls asleep
[1518-04-22 00:55] wakes up
[1518-10-07 00:54] falls asleep
[1518-11-02 00:20] wakes up
[1518-10-30 00:32] falls asleep
[1518-05-06 00:00] Guard #863 begins shift
[1518-03-10 00:59] wakes up
[1518-09-19 00:59] wakes up
[1518-06-07 00:35] falls asleep
[1518-04-21 23:49] Guard #3209 begins shift
[1518-07-07 00:47] wakes up
[1518-04-09 00:45] wakes up
[1518-09-06 00:45] falls asleep
[1518-03-26 00:34] wakes up
[1518-03-03 00:01] Guard #419 begins shift
[1518-10-11 00:21] falls asleep
[1518-09-20 00:33] falls asleep
[1518-07-15 00:24] falls asleep
[1518-03-17 00:40] wakes up
[1518-05-23 00:46] falls asleep
[1518-03-20 00:40] wakes up
[1518-11-11 00:55] wakes up
[1518-07-12 00:03] Guard #2143 begins shift
[1518-08-16 00:13] falls asleep
[1518-05-13 00:41] wakes up
[1518-04-18 00:58] wakes up
[1518-09-01 00:59] wakes up
[1518-05-05 00:37] falls asleep
[1518-09-09 00:02] Guard #521 begins shift
[1518-06-09 00:44] falls asleep
[1518-02-12 00:44] wakes up
[1518-05-26 00:40] wakes up
[1518-09-04 00:37] falls asleep
[1518-09-11 00:54] wakes up
[1518-08-01 00:02] falls asleep
[1518-07-03 00:43] wakes up
[1518-11-10 00:09] falls asleep
[1518-10-14 00:33] wakes up
[1518-04-21 00:47] wakes up
[1518-02-03 23:59] Guard #1999 begins shift
[1518-10-05 00:47] falls asleep
[1518-03-18 00:04] Guard #431 begins shift
[1518-01-28 00:00] Guard #3209 begins shift
[1518-08-09 00:52] wakes up
[1518-10-03 00:55] wakes up
[1518-10-20 00:03] Guard #863 begins shift
[1518-08-17 00:03] Guard #2539 begins shift
[1518-10-26 00:02] Guard #751 begins shift
[1518-07-16 23:49] Guard #419 begins shift
[1518-09-24 00:55] falls asleep
[1518-03-06 00:42] falls asleep
[1518-06-13 23:50] Guard #3209 begins shift
[1518-07-08 00:17] falls asleep
[1518-05-23 23:50] Guard #1627 begins shift
[1518-03-07 00:07] falls asleep
[1518-04-07 00:31] falls asleep
[1518-05-15 00:39] wakes up
[1518-06-01 00:27] falls asleep
[1518-07-17 23:51] Guard #1637 begins shift
[1518-02-07 00:48] falls asleep
[1518-03-14 00:18] wakes up
[1518-02-07 00:51] wakes up
[1518-07-31 23:47] Guard #863 begins shift
[1518-08-21 00:47] wakes up
[1518-05-05 00:57] wakes up
[1518-10-24 23:56] Guard #863 begins shift
[1518-10-19 00:58] wakes up
[1518-10-01 23:58] Guard #431 begins shift
[1518-02-23 00:39] falls asleep
[1518-02-04 23:58] Guard #601 begins shift
[1518-07-06 00:50] wakes up
[1518-08-09 00:14] wakes up
[1518-08-05 23:51] Guard #373 begins shift
[1518-02-11 00:26] falls asleep
[1518-11-03 00:37] falls asleep
[1518-05-12 00:11] falls asleep
[1518-02-09 00:39] wakes up
[1518-02-05 00:45] falls asleep
[1518-01-20 00:49] wakes up
[1518-10-23 00:56] wakes up
[1518-08-15 00:13] falls asleep
[1518-02-06 00:33] wakes up
[1518-10-12 00:47] wakes up
[1518-03-21 00:02] Guard #991 begins shift
[1518-08-15 00:52] falls asleep
[1518-06-16 00:10] wakes up
[1518-11-20 00:06] falls asleep
[1518-03-24 00:25] falls asleep
[1518-05-25 00:57] wakes up
[1518-01-21 00:00] Guard #2857 begins shift
[1518-02-24 00:54] falls asleep
[1518-04-02 00:27] wakes up
[1518-10-14 00:36] falls asleep
[1518-02-16 00:04] falls asleep
[1518-08-24 00:47] wakes up
[1518-05-04 00:54] wakes up
[1518-03-17 00:46] falls asleep
[1518-02-17 00:48] falls asleep
[1518-02-24 00:04] Guard #419 begins shift
[1518-02-10 00:46] falls asleep
[1518-02-28 23:59] Guard #173 begins shift
[1518-06-17 00:04] Guard #523 begins shift
[1518-04-07 00:56] wakes up
[1518-07-17 00:02] falls asleep
[1518-05-28 00:33] wakes up
[1518-06-17 23:58] Guard #751 begins shift
[1518-02-09 00:34] falls asleep
[1518-06-15 00:08] falls asleep
[1518-05-17 23:58] Guard #521 begins shift
[1518-01-25 23:57] Guard #3229 begins shift
[1518-03-09 00:59] wakes up
[1518-10-01 00:51] wakes up
[1518-03-01 00:40] falls asleep
[1518-05-28 00:41] wakes up
[1518-02-25 00:00] Guard #2143 begins shift
[1518-08-16 00:57] wakes up
[1518-07-08 00:57] falls asleep
[1518-05-06 00:56] wakes up
[1518-05-09 00:45] falls asleep
[1518-04-25 00:40] falls asleep
[1518-06-13 00:35] wakes up
[1518-08-15 00:24] wakes up
[1518-07-06 00:49] falls asleep
[1518-08-10 00:53] wakes up
[1518-06-05 00:52] wakes up
[1518-05-31 00:35] falls asleep
[1518-03-05 00:03] Guard #2857 begins shift
[1518-04-10 00:15] wakes up
[1518-05-22 23:51] Guard #1597 begins shift
[1518-09-23 00:03] Guard #431 begins shift
[1518-07-12 00:40] falls asleep
[1518-05-29 00:36] wakes up
[1518-03-24 00:01] falls asleep
[1518-08-17 23:57] Guard #3187 begins shift
[1518-08-19 00:07] falls asleep
[1518-06-27 00:58] wakes up
[1518-10-21 00:55] falls asleep
[1518-01-31 00:51] wakes up
[1518-09-02 23:58] Guard #3229 begins shift
[1518-02-10 23:57] Guard #2539 begins shift
[1518-07-21 00:01] Guard #1637 begins shift
[1518-03-30 00:23] falls asleep
[1518-08-25 00:15] falls asleep
[1518-04-01 23:50] Guard #1637 begins shift
[1518-06-17 00:27] wakes up
[1518-07-02 00:16] wakes up
[1518-08-31 00:08] falls asleep
[1518-04-30 00:10] falls asleep
[1518-08-14 00:35] wakes up
[1518-04-01 00:54] falls asleep
[1518-07-18 00:32] falls asleep
[1518-06-12 00:45] wakes up
[1518-05-02 00:30] wakes up
[1518-04-26 00:24] falls asleep
[1518-04-12 00:51] falls asleep
[1518-09-19 00:46] wakes up
[1518-08-30 23:57] Guard #1627 begins shift
[1518-04-21 00:50] falls asleep
[1518-05-22 00:09] falls asleep
[1518-05-10 00:20] falls asleep
[1518-04-08 00:22] falls asleep
[1518-07-17 00:45] wakes up
[1518-07-25 00:32] falls asleep
[1518-04-07 00:35] wakes up
[1518-04-30 00:25] wakes up
[1518-10-31 00:41] falls asleep
[1518-08-15 00:56] wakes up
[1518-08-16 00:01] Guard #2539 begins shift
[1518-02-20 00:33] wakes up
[1518-06-09 00:26] falls asleep
[1518-07-11 00:37] falls asleep
[1518-07-18 00:00] falls asleep
[1518-08-16 00:51] falls asleep
[1518-10-18 00:00] Guard #991 begins shift
[1518-06-01 00:18] falls asleep
[1518-01-14 00:54] falls asleep
[1518-09-06 00:57] wakes up
[1518-05-23 00:35] wakes up
[1518-04-06 00:51] wakes up
[1518-02-21 00:00] Guard #2143 begins shift
[1518-03-04 00:04] Guard #2857 begins shift
[1518-02-12 00:01] falls asleep
[1518-06-28 00:16] wakes up
[1518-06-19 00:34] wakes up
[1518-08-01 00:52] wakes up
[1518-07-27 00:02] Guard #419 begins shift
[1518-09-05 00:44] wakes up
[1518-09-13 00:05] falls asleep
[1518-11-14 23:59] Guard #1597 begins shift
[1518-09-28 00:44] wakes up
[1518-02-07 00:44] wakes up
[1518-03-05 23:57] Guard #523 begins shift
[1518-10-03 00:39] wakes up
[1518-08-04 00:03] Guard #2339 begins shift
[1518-10-05 00:55] wakes up
[1518-06-14 00:03] falls asleep
[1518-08-22 23:59] Guard #601 begins shift
[1518-04-26 00:01] falls asleep
[1518-06-03 00:01] falls asleep
[1518-03-06 23:57] Guard #2857 begins shift
[1518-08-17 00:56] falls asleep
[1518-05-03 00:13] falls asleep
[1518-11-04 00:54] wakes up
[1518-01-30 00:35] wakes up
[1518-04-28 00:58] wakes up
[1518-04-03 00:01] Guard #3209 begins shift
[1518-09-09 00:11] falls asleep
[1518-05-21 00:00] Guard #2339 begins shift
[1518-05-27 00:54] wakes up
[1518-01-30 00:51] falls asleep
[1518-04-17 00:57] wakes up
[1518-01-16 00:04] Guard #2339 begins shift
[1518-03-19 00:54] falls asleep
[1518-04-20 00:33] wakes up
[1518-05-19 00:48] falls asleep
[1518-06-05 00:56] falls asleep
[1518-04-27 00:56] wakes up
[1518-04-19 23:47] Guard #521 begins shift
[1518-02-25 23:57] Guard #829 begins shift
[1518-01-22 00:42] wakes up
[1518-08-24 00:31] falls asleep
[1518-04-18 00:09] falls asleep
[1518-05-16 00:38] wakes up
[1518-05-12 23:59] Guard #373 begins shift
[1518-05-20 00:43] wakes up
[1518-04-18 00:54] falls asleep
[1518-03-30 23:59] Guard #751 begins shift
[1518-03-08 00:59] wakes up
[1518-03-09 00:01] Guard #2143 begins shift
[1518-03-26 00:53] wakes up
[1518-05-13 23:54] Guard #523 begins shift
[1518-06-13 00:34] falls asleep
[1518-03-27 00:02] falls asleep
[1518-11-09 00:55] wakes up
[1518-02-05 00:57] falls asleep
[1518-02-05 00:27] wakes up
[1518-09-28 00:55] wakes up
[1518-03-20 00:51] wakes up
[1518-08-06 00:20] wakes up
[1518-04-16 23:59] Guard #1627 begins shift
[1518-10-18 23:56] Guard #431 begins shift
[1518-07-21 00:52] falls asleep
[1518-05-19 00:36] falls asleep
[1518-04-12 23:48] Guard #173 begins shift
[1518-05-07 00:37] falls asleep
[1518-10-04 00:53] falls asleep
[1518-06-26 00:36] falls asleep
[1518-04-04 00:52] wakes up
[1518-05-04 00:04] Guard #3229 begins shift
[1518-07-09 00:38] falls asleep
[1518-05-01 00:32] wakes up
[1518-05-02 00:27] falls asleep
'''

rows = inp.strip().split('\n')
rows.sort()

# guard id -> mins asleep total
minutes_asleep = Counter()
# guard id -> counter of minutes slept
common_mins = defaultdict(Counter)

def min_counts(begind, endd):
    curr = datetime.datetime(*begind)
    end_d = datetime.datetime(*endd)
    seq = Counter()
    while curr < end_d:
        seq[curr.minute] += 1
        curr += datetime.timedelta(minutes=1)
    return seq

def minutes_apart(begind, endd):
    return (datetime.datetime(*endd) - datetime.datetime(*begind)).total_seconds() / 60

def add_counts(base, op):
    for k, v in op.items():
        base[k] += v


# state as we iterate
curr_guard = None
last_time = None

for row in rows:
    parts = row.split()
    year, month, day = [int(part) for part in parts[0][1:].split('-')]
    hour, min = [int(part) for part in parts[1][:-1].split(':')]
    date_p = (year, month, day, hour, min)
    rest = parts[2:]
    if rest[0] == 'Guard':
        guard = int(rest[1][1:])
        curr_guard = guard
        last_time = date_p
    elif rest[0] == 'falls':
        last_time = date_p
    else:
        assert rest[0] == 'wakes'
        counts = min_counts(last_time, date_p)
        add_counts(common_mins[curr_guard], counts)
        minutes_asleep[curr_guard] += minutes_apart(last_time, date_p)
        last_time = date_p

# part 1
most_asleep_guard = minutes_asleep.most_common(1)[0][0]
most_common_minute = common_mins[guard].most_common(1)[0][0]
print most_asleep_guard * most_common_minute

# part 2
max_count = -1
max_minute = None
max_guard = None
for guard, counts in common_mins.iteritems():
    for minute, count in counts.iteritems():
        if count > max_count:
            max_count = count
            max_minute = minute
            max_guard = guard

print max_guard * max_minute
