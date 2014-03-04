# TCP Plotting using Python

This code shows some examples of how to create plots that demonstrate
the effectiveness of a TCP implementation. The plots are:

* rate.png : Shows the rate of the TCP connection over time. The rate is
  smoothed by summing all the bytes received over a 1 second window,
  then sliding this window in 0.1 second increments.

* queue.png: Shows the queue size of a router over time. Dropped packets
  are plotted with an "X" symbol at the maximum queue size plus 1.

* sequence.png: Shows a sequence number plot over time. A square box
  is plotted at each (time,sequence) pair, and a dot is plotted at
  each (time,acknumber) pair. The sequence numbers are divided by 1500
  to convert bytes to packets, and modded by 50 to wrap the graph
  horizontally.

## Generation scripts:

* generate-rates.py
* generate-queue.py

These generate the rates.txt and queue.txt files, respectively. This is
artificial data to mimic traces from a TCP implementation and a router.
The resulting data is not intended to be accurate but to show how the
plotting works.

## Plotting scripts

* plot-rate.py
* plot-queue.py
* plot-sequence.py

These generate the graphs described above, using the data files created by
the generation scripts.

### Installation Requirements


hese examples require the installation of matplotlib. You can easily
install this using:

```
sudo apt-get install python-pip
sudo pip install matplotlib
```

If you wish to use a virtual environment instead, then use the
following to create and activate a virtual environment with the
required packages.

```
sudo apt-get install python-pip
sudo pip install virtualenv
mkdir ~/virtualenvs
virtualenv ~/virtualenvs/plotting
source ~/virtualenvs/plotting/bin/activate
pip install -r requirements.txt
```

