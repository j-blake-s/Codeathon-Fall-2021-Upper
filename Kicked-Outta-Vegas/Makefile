NUMSAMPLES=3
MAXTEST=15

ZIP=testcases.zip

define mktests
$(patsubst %,$(1)/$(1)%.txt,$(shell seq -f "%02.f" $(2) $(3)))
endef

all: tests

inputs: $(call mktests,input,0,$(MAXTEST))
tests: inputs $(call mktests,output,0,$(MAXTEST))
zip: $(ZIP)

$(ZIP): $(call mktests,input,0,$(MAXTEST)) $(call mktests,output,0,$(MAXTEST))
	zip -r $@ $^

dbg:
	echo $(call mktests,input,0,$(MAXTEST))

input/input%.txt: testgen.py
	python $< --debug $* $(MAXTEST) > $@

output/output%.txt: solutions/solution.py input/input%.txt
	python $< < $(filter-out $<,$^) > $@

clean:
	rm -f $(ZIP) \
	      $(call mktests,input,$(NUMSAMPLES),$(MAXTEST)) \
	      $(call mktests,output,$(NUMSAMPLES),$(MAXTEST))
