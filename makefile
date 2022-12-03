runDay: $(dayNumber)
	echo "Running: " $(dayNumber)
	python /Day$(dayNumber)/main.py

# generateDay: $(dayNumber)
# 	echo "Generating day " $dayNumber) "..."
# 	python /util/generateDay.py $(dayNumber)