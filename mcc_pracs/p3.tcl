 set ns [new Simulator -multicast on]; # enable multicast routing;
set group [Node allocaddr]  ; # allocate a multicast address;
set node0 [$ns node]         ;# create multicast capable nodes;
set node1 [$ns node]
$ns duplex-link $node0 $node1 1.5Mb 10ms DropTail

set tracef [open dm.tr w]
$ns trace-all $tracef

set namtracef [open dm.nam w]
$ns namtrace-all $namtracef

set mproto DM         ; # configure multicast protocol;
set mrthandle [$ns mrtproto $mproto]; # all nodes will contain multicast protocol agents;

set udp [new Agent/UDP]         ;# create a source agent at node 0;
$ns attach-agent $node0 $udp
set cbr [new Application/Traffic/CBR]       
$cbr attach-agent $udp
$udp set dst_addr_ $group
$udp set dst_port_ 0

set receiver [new Agent/LossMonitor];  # create a receiver agent at node 1;
$ns attach-agent $node1 $receiver
$ns at 0.3 "$node1 join-group $receiver $group"
$ns at 0.1 "$cbr start"

$ns at 5.0 "finish"

proc finish {} {
       global ns tracef namtracef
       exec nam dm.nam &
       close $tracef
       close $namtracef
       exit 0
}
$ns run