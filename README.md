# systemd-date-time-service
This repo act's like a guideline to setting up a systemd service.

# The script to be referenced in the .service file
Start by creating you script (basically any piece of code).
As an example, I've decided to write a simple python code that get's the date and time and write's it into a file (obviously this isn't about python, nor is it python specific).

# Testing

You can test the program before creating it's service the following way:

``` python3 date_time_test.py```

You should see the date and time in the newly created file ```TEST.txt``` by using ```cat TEST.txt```

# Creating .service file

Navigate to your root directory (```cd //```), then ```cd etc/systemd/system/```, and create a new file with the ```.service``` suffix (i.e ```touch my_service.service```).

For all the flags and options available to the .service file, please refer to https://www.freedesktop.org/software/systemd/man/systemd.service.html

In the service section, you'll need to set your own User ans ExecStart variables. To find your user, execute ```echo $USER```:

User=<YOUR_USER>

The first argument of ExecStart describes the path to the interpreter that you're looking to use. In my case, since I have a ```.py``` file, I want to give the path to my python3 executable which can be found this way:

```which python3``` -> ```usr/bin/python3```

The second argument then specifies the path of the program to run. A simple ```pwd``` in the shell should give you the path to your script (given you're running this command in the same directory as your script).

ExecStart=<path/to/python>  <path/to/date_time_test.py>

The service is to be restarted each 5 seconds, as indicated by ```RestartSec=5```.

# Setting up the service with systemd

In your ```etc/systemd/system/``` directory, run the following in your sheel:

```(sudo) systemctl daemon-reload```, which restart's the system-daemon, allowing your newly created service to be used (this should be done each time you bring modifications to .service files).

To run your service, go as following:

```(sudo) systemctl start my-service.service```

OR 

If you want to see the processing of you service via the journal of your systemd (```journalctl``` is used to query the contents of the systemd journal):

```(sudo) systemctl start my-service.service; journalctl -u my-service.service -f```

To stop your service:

```(sudo) systemctl stop my-service.service```



For this specific example, you can ```cat TEST.txt``` in the same directory as the ```date_time_test.py```. You should see the time update each 5 seconds, since we ask the service to restart after 5s.


