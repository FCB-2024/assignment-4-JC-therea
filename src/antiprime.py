## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
def main(inputVal) :
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT
	intInput = int(inputVal)

	divi = 0
	loop = 1
	while loop <= intInput:
		if intInput % loop == 0:
			divi = divi + 1
		loop = loop + 1

	minorValues = 1
	smallerDivi = 0

	while minorValues < intInput:
		smallerDiviLocal = 0
		loop = 1
		while loop <= minorValues:
			if minorValues % loop == 0:
				smallerDiviLocal = smallerDiviLocal + 1
			if smallerDiviLocal > smallerDivi:
				smallerDivi = smallerDiviLocal
			loop = loop + 1


		minorValues = minorValues + 1

	if smallerDivi < divi:
		return("anti-prime")
	else:
		return("not anti-prime")

import sys

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :
	x = int(sys.argv[1])
	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	## SOUGHT DINUCLEOTIDE.
	print(main(x))
