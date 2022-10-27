"""
    pygments.lexers._csound_builtins
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2006-2022 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

REMOVED_OPCODES = set('''
OSCsendA
beadsynt
beosc
buchla
getrowlin
lua_exec
lua_iaopcall
lua_iaopcall_off
lua_ikopcall
lua_ikopcall_off
lua_iopcall
lua_iopcall_off
lua_opdef
mp3scal_check
mp3scal_load
mp3scal_load2
mp3scal_play
mp3scal_play2
pvsgendy
socksend_k
signalflowgraph
sumTableFilter
systime
tabrowlin
vbap1move
'''.split())

# Opcodes in Csound 6.17.0 using:
#   python3 -c "
#   import regex as re
#   from subprocess import Popen, PIPE
#   output = Popen(['csound', '--list-opcodes0'], stderr=PIPE, text=True).communicate()[1]
#   opcodes = output[re.search(r'^\$', output, re.M).end() : re.search(r'^\d+ opcodes\$', output, re.M).start()].split()
#   output = Popen(['csound', '--list-opcodes2'], stderr=PIPE, text=True).communicate()[1]
#   all_opcodes = output[re.search(r'^\$', output, re.M).end() : re.search(r'^\d+ opcodes\$', output, re.M).start()].split()
#   deprecated_opcodes = [opcode for opcode in all_opcodes if opcode not in opcodes]
#   # Remove opcodes that csound.py treats as keywords.
#   keyword_opcodes = [
#       'cggoto',   # https://csound.com/docs/manual/cggoto.html
#       'cigoto',   # https://csound.com/docs/manual/cigoto.html
#       'cingoto',  # (undocumented)
#       'ckgoto',   # https://csound.com/docs/manual/ckgoto.html
#       'cngoto',   # https://csound.com/docs/manual/cngoto.html
#       'cnkgoto',  # (undocumented)
#       'endin',    # https://csound.com/docs/manual/endin.html
#       'endop',    # https://csound.com/docs/manual/endop.html
#       'goto',     # https://csound.com/docs/manual/goto.html
#       'igoto',    # https://csound.com/docs/manual/igoto.html
#       'instr',    # https://csound.com/docs/manual/instr.html
#       'kgoto',    # https://csound.com/docs/manual/kgoto.html
#       'loop_ge',  # https://csound.com/docs/manual/loop_ge.html
#       'loop_gt',  # https://csound.com/docs/manual/loop_gt.html
#       'loop_le',  # https://csound.com/docs/manual/loop_le.html
#       'loop_lt',  # https://csound.com/docs/manual/loop_lt.html
#       'opcode',   # https://csound.com/docs/manual/opcode.html
#       'reinit',   # https://csound.com/docs/manual/reinit.html
#       'return',   # https://csound.com/docs/manual/return.html
#       'rireturn', # https://csound.com/docs/manual/rireturn.html
#       'rigoto',   # https://csound.com/docs/manual/rigoto.html
#       'tigoto',   # https://csound.com/docs/manual/tigoto.html
#       'timout'    # https://csound.com/docs/manual/timout.html
#   ]
#   opcodes = [opcode for opcode in opcodes if opcode not in keyword_opcodes]
#   newline = '\n'
#   print(f'''OPCODES = set(\'''
#   {newline.join(opcodes)}
#   \'''.split())
#
#   DEPRECATED_OPCODES = set(\'''
#   {newline.join(deprecated_opcodes)}
#   \'''.split())
#   ''')
#   "

OPCODES = set('''
ATSadd
ATSaddnz
ATSbufread
ATScross
ATSinfo
ATSinterpread
ATSpartialtap
ATSread
ATSreadnz
ATSsinnoi
FLbox
FLbutBank
FLbutton
FLcloseButton
FLcolor
FLcolor2
FLcount
FLexecButton
FLgetsnap
FLgroup
FLgroupEnd
FLgroup_end
FLhide
FLhvsBox
FLhvsBoxSetValue
FLjoy
FLkeyIn
FLknob
FLlabel
FLloadsnap
FLmouse
FLpack
FLpackEnd
FLpack_end
FLpanel
FLpanelEnd
FLpanel_end
FLprintk
FLprintk2
FLroller
FLrun
FLsavesnap
FLscroll
FLscrollEnd
FLscroll_end
FLsetAlign
FLsetBox
FLsetColor
FLsetColor2
FLsetFont
FLsetPosition
FLsetSize
FLsetSnapGroup
FLsetText
FLsetTextColor
FLsetTextSize
FLsetTextType
FLsetVal
FLsetVal_i
FLsetVali
FLsetsnap
FLshow
FLslidBnk
FLslidBnk2
FLslidBnk2Set
FLslidBnk2Setk
FLslidBnkGetHandle
FLslidBnkSet
FLslidBnkSetk
FLslider
FLtabs
FLtabsEnd
FLtabs_end
FLtext
FLupdate
FLvalue
FLvkeybd
FLvslidBnk
FLvslidBnk2
FLxyin
JackoAudioIn
JackoAudioInConnect
JackoAudioOut
JackoAudioOutConnect
JackoFreewheel
JackoInfo
JackoInit
JackoMidiInConnect
JackoMidiOut
JackoMidiOutConnect
JackoNoteOut
JackoOn
JackoTransport
K35_hpf
K35_lpf
MixerClear
MixerGetLevel
MixerReceive
MixerSend
MixerSetLevel
MixerSetLevel_i
OSCbundle
OSCcount
OSCinit
OSCinitM
OSClisten
OSCraw
OSCsend
OSCsend_lo
S
STKBandedWG
STKBeeThree
STKBlowBotl
STKBlowHole
STKBowed
STKBrass
STKClarinet
STKDrummer
STKFMVoices
STKFlute
STKHevyMetl
STKMandolin
STKModalBar
STKMoog
STKPercFlut
STKPlucked
STKResonate
STKRhodey
STKSaxofony
STKShakers
STKSimple
STKSitar
STKStifKarp
STKTubeBell
STKVoicForm
STKWhistle
STKWurley
a
abs
active
adsr
adsyn
adsynt
adsynt2
aftouch
allpole
alpass
alwayson
ampdb
ampdbfs
ampmidi
ampmidicurve
ampmidid
apoleparams
arduinoRead
arduinoReadF
arduinoStart
arduinoStop
areson
aresonk
atone
atonek
atonex
autocorr
babo
balance
balance2
bamboo
barmodel
bbcutm
bbcuts
betarand
bexprnd
bformdec1
bformdec2
bformenc1
binit
biquad
biquada
birnd
bob
bpf
bpfcos
bqrez
butbp
butbr
buthp
butlp
butterbp
butterbr
butterhp
butterlp
button
buzz
c2r
cabasa
cauchy
cauchyi
cbrt
ceil
cell
cent
centroid
ceps
cepsinv
chanctrl
changed
changed2
chani
chano
chebyshevpoly
checkbox
chn_S
chn_a
chn_k
chnclear
chnexport
chnget
chngeta
chngeti
chngetk
chngetks
chngets
chnmix
chnparams
chnset
chnseta
chnseti
chnsetk
chnsetks
chnsets
chuap
clear
clfilt
clip
clockoff
clockon
cmp
cmplxprod
cntCreate
cntCycles
cntDelete
cntDelete_i
cntRead
cntReset
cntState
comb
combinv
compilecsd
compileorc
compilestr
compress
compress2
connect
control
convle
convolve
copya2ftab
copyf2array
cos
cosh
cosinv
cosseg
cossegb
cossegr
count
count_i
cps2pch
cpsmidi
cpsmidib
cpsmidinn
cpsoct
cpspch
cpstmid
cpstun
cpstuni
cpsxpch
cpumeter
cpuprc
cross2
crossfm
crossfmi
crossfmpm
crossfmpmi
crosspm
crosspmi
crunch
ctlchn
ctrl14
ctrl21
ctrl7
ctrlinit
ctrlpreset
ctrlprint
ctrlprintpresets
ctrlsave
ctrlselect
cuserrnd
dam
date
dates
db
dbamp
dbfsamp
dcblock
dcblock2
dconv
dct
dctinv
deinterleave
delay
delay1
delayk
delayr
delayw
deltap
deltap3
deltapi
deltapn
deltapx
deltapxw
denorm
diff
diode_ladder
directory
diskgrain
diskin
diskin2
dispfft
display
distort
distort1
divz
doppler
dot
downsamp
dripwater
dssiactivate
dssiaudio
dssictls
dssiinit
dssilist
dumpk
dumpk2
dumpk3
dumpk4
duserrnd
dust
dust2
envlpx
envlpxr
ephasor
eqfil
evalstr
event
event_i
exciter
exitnow
exp
expcurve
expon
exprand
exprandi
expseg
expsega
expsegb
expsegba
expsegr
fareylen
fareyleni
faustaudio
faustcompile
faustctl
faustdsp
faustgen
faustplay
fft
fftinv
ficlose
filebit
filelen
filenchnls
filepeak
filescal
filesr
filevalid
fillarray
filter2
fin
fini
fink
fiopen
flanger
flashtxt
flooper
flooper2
floor
fluidAllOut
fluidCCi
fluidCCk
fluidControl
fluidEngine
fluidInfo
fluidLoad
fluidNote
fluidOut
fluidProgramSelect
fluidSetInterpMethod
fmanal
fmax
fmb3
fmbell
fmin
fmmetal
fmod
fmpercfl
fmrhode
fmvoice
fmwurlie
fof
fof2
fofilter
fog
fold
follow
follow2
foscil
foscili
fout
fouti
foutir
foutk
fprintks
fprints
frac
fractalnoise
framebuffer
freeverb
ftaudio
ftchnls
ftconv
ftcps
ftexists
ftfree
ftgen
ftgenonce
ftgentmp
ftlen
ftload
ftloadk
ftlptim
ftmorf
ftom
ftprint
ftresize
ftresizei
ftsamplebank
ftsave
ftsavek
ftset
ftslice
ftslicei
ftsr
gain
gainslider
gauss
gaussi
gausstrig
gbuzz
genarray
genarray_i
gendy
gendyc
gendyx
getcfg
getcol
getftargs
getrow
getseed
gogobel
grain
grain2
grain3
granule
gtadsr
gtf
guiro
harmon
harmon2
harmon3
harmon4
hdf5read
hdf5write
hilbert
hilbert2
hrtfearly
hrtfmove
hrtfmove2
hrtfreverb
hrtfstat
hsboscil
hvs1
hvs2
hvs3
hypot
i
ihold
imagecreate
imagefree
imagegetpixel
imageload
imagesave
imagesetpixel
imagesize
in
in32
inch
inh
init
initc14
initc21
initc7
inleta
inletf
inletk
inletkid
inletv
ino
inq
inrg
ins
insglobal
insremot
int
integ
interleave
interp
invalue
inx
inz
jacktransport
jitter
jitter2
joystick
jspline
k
la_i_add_mc
la_i_add_mr
la_i_add_vc
la_i_add_vr
la_i_assign_mc
la_i_assign_mr
la_i_assign_t
la_i_assign_vc
la_i_assign_vr
la_i_conjugate_mc
la_i_conjugate_mr
la_i_conjugate_vc
la_i_conjugate_vr
la_i_distance_vc
la_i_distance_vr
la_i_divide_mc
la_i_divide_mr
la_i_divide_vc
la_i_divide_vr
la_i_dot_mc
la_i_dot_mc_vc
la_i_dot_mr
la_i_dot_mr_vr
la_i_dot_vc
la_i_dot_vr
la_i_get_mc
la_i_get_mr
la_i_get_vc
la_i_get_vr
la_i_invert_mc
la_i_invert_mr
la_i_lower_solve_mc
la_i_lower_solve_mr
la_i_lu_det_mc
la_i_lu_det_mr
la_i_lu_factor_mc
la_i_lu_factor_mr
la_i_lu_solve_mc
la_i_lu_solve_mr
la_i_mc_create
la_i_mc_set
la_i_mr_create
la_i_mr_set
la_i_multiply_mc
la_i_multiply_mr
la_i_multiply_vc
la_i_multiply_vr
la_i_norm1_mc
la_i_norm1_mr
la_i_norm1_vc
la_i_norm1_vr
la_i_norm_euclid_mc
la_i_norm_euclid_mr
la_i_norm_euclid_vc
la_i_norm_euclid_vr
la_i_norm_inf_mc
la_i_norm_inf_mr
la_i_norm_inf_vc
la_i_norm_inf_vr
la_i_norm_max_mc
la_i_norm_max_mr
la_i_print_mc
la_i_print_mr
la_i_print_vc
la_i_print_vr
la_i_qr_eigen_mc
la_i_qr_eigen_mr
la_i_qr_factor_mc
la_i_qr_factor_mr
la_i_qr_sym_eigen_mc
la_i_qr_sym_eigen_mr
la_i_random_mc
la_i_random_mr
la_i_random_vc
la_i_random_vr
la_i_size_mc
la_i_size_mr
la_i_size_vc
la_i_size_vr
la_i_subtract_mc
la_i_subtract_mr
la_i_subtract_vc
la_i_subtract_vr
la_i_t_assign
la_i_trace_mc
la_i_trace_mr
la_i_transpose_mc
la_i_transpose_mr
la_i_upper_solve_mc
la_i_upper_solve_mr
la_i_vc_create
la_i_vc_set
la_i_vr_create
la_i_vr_set
la_k_a_assign
la_k_add_mc
la_k_add_mr
la_k_add_vc
la_k_add_vr
la_k_assign_a
la_k_assign_f
la_k_assign_mc
la_k_assign_mr
la_k_assign_t
la_k_assign_vc
la_k_assign_vr
la_k_conjugate_mc
la_k_conjugate_mr
la_k_conjugate_vc
la_k_conjugate_vr
la_k_current_f
la_k_current_vr
la_k_distance_vc
la_k_distance_vr
la_k_divide_mc
la_k_divide_mr
la_k_divide_vc
la_k_divide_vr
la_k_dot_mc
la_k_dot_mc_vc
la_k_dot_mr
la_k_dot_mr_vr
la_k_dot_vc
la_k_dot_vr
la_k_f_assign
la_k_get_mc
la_k_get_mr
la_k_get_vc
la_k_get_vr
la_k_invert_mc
la_k_invert_mr
la_k_lower_solve_mc
la_k_lower_solve_mr
la_k_lu_det_mc
la_k_lu_det_mr
la_k_lu_factor_mc
la_k_lu_factor_mr
la_k_lu_solve_mc
la_k_lu_solve_mr
la_k_mc_set
la_k_mr_set
la_k_multiply_mc
la_k_multiply_mr
la_k_multiply_vc
la_k_multiply_vr
la_k_norm1_mc
la_k_norm1_mr
la_k_norm1_vc
la_k_norm1_vr
la_k_norm_euclid_mc
la_k_norm_euclid_mr
la_k_norm_euclid_vc
la_k_norm_euclid_vr
la_k_norm_inf_mc
la_k_norm_inf_mr
la_k_norm_inf_vc
la_k_norm_inf_vr
la_k_norm_max_mc
la_k_norm_max_mr
la_k_qr_eigen_mc
la_k_qr_eigen_mr
la_k_qr_factor_mc
la_k_qr_factor_mr
la_k_qr_sym_eigen_mc
la_k_qr_sym_eigen_mr
la_k_random_mc
la_k_random_mr
la_k_random_vc
la_k_random_vr
la_k_subtract_mc
la_k_subtract_mr
la_k_subtract_vc
la_k_subtract_vr
la_k_t_assign
la_k_trace_mc
la_k_trace_mr
la_k_upper_solve_mc
la_k_upper_solve_mr
la_k_vc_set
la_k_vr_set
lag
lagud
lastcycle
lenarray
lfo
lfsr
limit
limit1
lincos
line
linen
linenr
lineto
link_beat_force
link_beat_get
link_beat_request
link_create
link_enable
link_is_enabled
link_metro
link_peers
link_tempo_get
link_tempo_set
linlin
linrand
linseg
linsegb
linsegr
liveconv
locsend
locsig
log
log10
log2
logbtwo
logcurve
loopseg
loopsegp
looptseg
loopxseg
lorenz
loscil
loscil3
loscil3phs
loscilphs
loscilx
lowpass2
lowres
lowresx
lpcanal
lpcfilter
lpf18
lpform
lpfreson
lphasor
lpinterp
lposcil
lposcil3
lposcila
lposcilsa
lposcilsa2
lpread
lpreson
lpshold
lpsholdp
lpslot
lufs
mac
maca
madsr
mags
mandel
mandol
maparray
maparray_i
marimba
massign
max
max_k
maxabs
maxabsaccum
maxaccum
maxalloc
maxarray
mclock
mdelay
median
mediank
metro
metro2
metrobpm
mfb
midglobal
midiarp
midic14
midic21
midic7
midichannelaftertouch
midichn
midicontrolchange
midictrl
mididefault
midifilestatus
midiin
midinoteoff
midinoteoncps
midinoteonkey
midinoteonoct
midinoteonpch
midion
midion2
midiout
midiout_i
midipgm
midipitchbend
midipolyaftertouch
midiprogramchange
miditempo
midremot
min
minabs
minabsaccum
minaccum
minarray
mincer
mirror
mode
modmatrix
monitor
moog
moogladder
moogladder2
moogvcf
moogvcf2
moscil
mp3bitrate
mp3in
mp3len
mp3nchnls
mp3out
mp3scal
mp3sr
mpulse
mrtmsg
ms2st
mtof
mton
multitap
mute
mvchpf
mvclpf1
mvclpf2
mvclpf3
mvclpf4
mvmfilter
mxadsr
nchnls_hw
nestedap
nlalp
nlfilt
nlfilt2
noise
noteoff
noteon
noteondur
noteondur2
notnum
nreverb
nrpn
nsamp
nstance
nstrnum
nstrstr
ntof
ntom
ntrpol
nxtpow2
octave
octcps
octmidi
octmidib
octmidinn
octpch
olabuffer
oscbnk
oscil
oscil1
oscil1i
oscil3
oscili
oscilikt
osciliktp
oscilikts
osciln
oscils
oscilx
out
out32
outall
outc
outch
outh
outiat
outic
outic14
outipat
outipb
outipc
outkat
outkc
outkc14
outkpat
outkpb
outkpc
outleta
outletf
outletk
outletkid
outletv
outo
outq
outq1
outq2
outq3
outq4
outrg
outs
outs1
outs2
outvalue
outx
outz
p
p5gconnect
p5gdata
pan
pan2
pareq
part2txt
partials
partikkel
partikkelget
partikkelset
partikkelsync
passign
paulstretch
pcauchy
pchbend
pchmidi
pchmidib
pchmidinn
pchoct
pchtom
pconvolve
pcount
pdclip
pdhalf
pdhalfy
peak
pgmassign
pgmchn
phaser1
phaser2
phasor
phasorbnk
phs
pindex
pinker
pinkish
pitch
pitchac
pitchamdf
planet
platerev
plltrack
pluck
poisson
pol2rect
polyaft
polynomial
port
portk
poscil
poscil3
pow
powershape
powoftwo
pows
prealloc
prepiano
print
print_type
printarray
printf
printf_i
printk
printk2
printks
printks2
println
prints
printsk
product
pset
ptablew
ptrack
puts
pvadd
pvbufread
pvcross
pvinterp
pvoc
pvread
pvs2array
pvs2tab
pvsadsyn
pvsanal
pvsarp
pvsbandp
pvsbandr
pvsbandwidth
pvsbin
pvsblur
pvsbuffer
pvsbufread
pvsbufread2
pvscale
pvscent
pvsceps
pvscfs
pvscross
pvsdemix
pvsdiskin
pvsdisp
pvsenvftw
pvsfilter
pvsfread
pvsfreeze
pvsfromarray
pvsftr
pvsftw
pvsfwrite
pvsgain
pvsgendy
pvshift
pvsifd
pvsin
pvsinfo
pvsinit
pvslock
pvslpc
pvsmaska
pvsmix
pvsmooth
pvsmorph
pvsosc
pvsout
pvspitch
pvstanal
pvstencil
pvstrace
pvsvoc
pvswarp
pvsynth
pwd
pyassign
pyassigni
pyassignt
pycall
pycall1
pycall1i
pycall1t
pycall2
pycall2i
pycall2t
pycall3
pycall3i
pycall3t
pycall4
pycall4i
pycall4t
pycall5
pycall5i
pycall5t
pycall6
pycall6i
pycall6t
pycall7
pycall7i
pycall7t
pycall8
pycall8i
pycall8t
pycalli
pycalln
pycallni
pycallt
pyeval
pyevali
pyevalt
pyexec
pyexeci
pyexect
pyinit
pylassign
pylassigni
pylassignt
pylcall
pylcall1
pylcall1i
pylcall1t
pylcall2
pylcall2i
pylcall2t
pylcall3
pylcall3i
pylcall3t
pylcall4
pylcall4i
pylcall4t
pylcall5
pylcall5i
pylcall5t
pylcall6
pylcall6i
pylcall6t
pylcall7
pylcall7i
pylcall7t
pylcall8
pylcall8i
pylcall8t
pylcalli
pylcalln
pylcallni
pylcallt
pyleval
pylevali
pylevalt
pylexec
pylexeci
pylexect
pylrun
pylruni
pylrunt
pyrun
pyruni
pyrunt
qinf
qnan
r2c
rand
randc
randh
randi
random
randomh
randomi
rbjeq
readclock
readf
readfi
readk
readk2
readk3
readk4
readks
readscore
readscratch
rect2pol
release
remoteport
remove
repluck
reshapearray
reson
resonbnk
resonk
resonr
resonx
resonxk
resony
resonz
resyn
reverb
reverb2
reverbsc
rewindscore
rezzy
rfft
rifft
rms
rnd
rnd31
rndseed
round
rspline
rtclock
s16b14
s32b14
samphold
sandpaper
sc_lag
sc_lagud
sc_phasor
sc_trig
scale
scale2
scalearray
scanhammer
scanmap
scans
scansmap
scantable
scanu
scanu2
schedkwhen
schedkwhennamed
schedule
schedulek
schedwhen
scoreline
scoreline_i
seed
sekere
select
semitone
sense
sensekey
seqtime
seqtime2
sequ
serialBegin
serialEnd
serialFlush
serialPrint
serialRead
serialWrite
serialWrite_i
setcol
setctrl
setksmps
setrow
setscorepos
sfilist
sfinstr
sfinstr3
sfinstr3m
sfinstrm
sfload
sflooper
sfpassign
sfplay
sfplay3
sfplay3m
sfplaym
sfplist
sfpreset
shaker
shiftin
shiftout
signum
sin
sinh
sininv
sinsyn
skf
sleighbells
slicearray
slicearray_i
slider16
slider16f
slider16table
slider16tablef
slider32
slider32f
slider32table
slider32tablef
slider64
slider64f
slider64table
slider64tablef
slider8
slider8f
slider8table
slider8tablef
sliderKawai
sndloop
sndwarp
sndwarpst
sockrecv
sockrecvs
socksend
socksends
sorta
sortd
soundin
space
spat3d
spat3di
spat3dt
spdist
spf
splitrig
sprintf
sprintfk
spsend
sqrt
squinewave
st2ms
statevar
sterrain
stix
strcat
strcatk
strchar
strchark
strcmp
strcmpk
strcpy
strcpyk
strecv
streson
strfromurl
strget
strindex
strindexk
string2array
strlen
strlenk
strlower
strlowerk
strrindex
strrindexk
strset
strstrip
strsub
strsubk
strtod
strtodk
strtol
strtolk
strupper
strupperk
stsend
subinstr
subinstrinit
sum
sumarray
svfilter
svn
syncgrain
syncloop
syncphasor
system
system_i
tab
tab2array
tab2pvs
tab_i
tabifd
table
table3
table3kt
tablecopy
tablefilter
tablefilteri
tablegpw
tablei
tableicopy
tableigpw
tableikt
tableimix
tablekt
tablemix
tableng
tablera
tableseg
tableshuffle
tableshufflei
tablew
tablewa
tablewkt
tablexkt
tablexseg
tabmorph
tabmorpha
tabmorphak
tabmorphi
tabplay
tabrec
tabsum
tabw
tabw_i
tambourine
tan
tanh
taninv
taninv2
tbvcf
tempest
tempo
temposcal
tempoval
timedseq
timeinstk
timeinsts
timek
times
tival
tlineto
tone
tonek
tonex
tradsyn
trandom
transeg
transegb
transegr
trcross
trfilter
trhighest
trigExpseg
trigLinseg
trigexpseg
trigger
trighold
triglinseg
trigphasor
trigseq
trim
trim_i
trirand
trlowest
trmix
trscale
trshift
trsplit
turnoff
turnoff2
turnoff2_i
turnoff3
turnon
tvconv
unirand
unwrap
upsamp
urandom
urd
vactrol
vadd
vadd_i
vaddv
vaddv_i
vaget
valpass
vaset
vbap
vbapg
vbapgmove
vbaplsinit
vbapmove
vbapz
vbapzmove
vcella
vclpf
vco
vco2
vco2ft
vco2ift
vco2init
vcomb
vcopy
vcopy_i
vdel_k
vdelay
vdelay3
vdelayk
vdelayx
vdelayxq
vdelayxs
vdelayxw
vdelayxwq
vdelayxws
vdivv
vdivv_i
vecdelay
veloc
vexp
vexp_i
vexpseg
vexpv
vexpv_i
vibes
vibr
vibrato
vincr
vlimit
vlinseg
vlowres
vmap
vmirror
vmult
vmult_i
vmultv
vmultv_i
voice
vosim
vphaseseg
vport
vpow
vpow_i
vpowv
vpowv_i
vps
vpvoc
vrandh
vrandi
vsubv
vsubv_i
vtaba
vtabi
vtabk
vtable1k
vtablea
vtablei
vtablek
vtablewa
vtablewi
vtablewk
vtabwa
vtabwi
vtabwk
vwrap
waveset
websocket
weibull
wgbow
wgbowedbar
wgbrass
wgclar
wgflute
wgpluck
wgpluck2
wguide1
wguide2
wiiconnect
wiidata
wiirange
wiisend
window
wrap
writescratch
wterrain
wterrain2
xadsr
xin
xout
xtratim
xyscale
zacl
zakinit
zamod
zar
zarg
zaw
zawm
zdf_1pole
zdf_1pole_mode
zdf_2pole
zdf_2pole_mode
zdf_ladder
zfilter2
zir
ziw
ziwm
zkcl
zkmod
zkr
zkw
zkwm
'''.split())

DEPRECATED_OPCODES = set('''
array
bformdec
bformenc
copy2ftab
copy2ttab
hrtfer
ktableseg
lentab
maxtab
mintab
pop
pop_f
ptable
ptable3
ptablei
ptableiw
push
push_f
scalet
sndload
soundout
soundouts
specaddm
specdiff
specdisp
specfilt
spechist
specptrk
specscal
specsum
spectrum
stack
sumtab
tabgen
tableiw
tabmap
tabmap_i
tabslice
tb0
tb0_init
tb1
tb10
tb10_init
tb11
tb11_init
tb12
tb12_init
tb13
tb13_init
tb14
tb14_init
tb15
tb15_init
tb1_init
tb2
tb2_init
tb3
tb3_init
tb4
tb4_init
tb5
tb5_init
tb6
tb6_init
tb7
tb7_init
tb8
tb8_init
tb9
tb9_init
vbap16
vbap4
vbap4move
vbap8
vbap8move
xscanmap
xscans
xscansmap
xscanu
xyin
'''.split())
