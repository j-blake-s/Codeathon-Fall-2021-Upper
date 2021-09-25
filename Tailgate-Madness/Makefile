NUMSAMPLES=3
MAXTEST=15
CXXFLAGS+= -g

define mktests
$(patsubst %,$(1)/$(1)%.txt,$(shell seq -f "%02.f" $(2) $(3)))
endef

define mkrule
build/%$(1): $(2) build
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) $(3) $< -o $@
endef

all: build/solution
debug: build/solution-debug
samples: $(call mktests,input,0,$$(($(NUMSAMPLES)-1))) \
         $(call mktests,output,0,$$(($(NUMSAMPLES)-1)))
inputs: $(call mktests,input,$(NUMSAMPLES),$(MAXTEST))
tests: samples inputs $(call mktests,output,0,$(MAXTEST))

input/input%.txt: build/testgen
	build/testgen $* $(MAXTEST) > $@

output/output%.txt: build/solution input/input%.txt
	$< < $(filter-out $<,$^) > $@

build:
	mkdir -p build

clean:
	rm -rf build/
	rm -f $(call mktests,input,$(NUMSAMPLES),$(MAXTEST)) \
	      $(call mktests,output,$(NUMSAMPLES),$(MAXTEST))

build/%: solutions/%.cpp build
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) $< -o $@

build/%-debug: solutions/%.cpp build
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) -DDEBUG $< -o $@

build/testgen: testgen.cpp build
	$(CXX) $(CPPFLAGS) $(CXXFLAGS) $< -o $@
