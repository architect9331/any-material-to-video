import {Audio} from "@remotion/media";
import {AbsoluteFill,Sequence,staticFile,useCurrentFrame,useVideoConfig} from "remotion";

type Segment={id:string;start:number;end:number;text:string};
type Timeline={duration:number;segments:Segment[]};
export type VideoProps={timeline:Timeline;voice?:string};

const Scene=({segment}:{segment:Segment})=> <AbsoluteFill style={{display:"grid",placeItems:"center",background:"#f4f0e6",color:"#121a2f",fontFamily:"system-ui"}}><div style={{fontSize:72,fontWeight:800,maxWidth:1400,textAlign:"center"}}>{segment.text}</div></AbsoluteFill>;

export const Video=({timeline,voice}:VideoProps)=>{const {fps}=useVideoConfig();const frame=useCurrentFrame();const active=timeline.segments.find(s=>frame>=s.start*fps&&frame<s.end*fps);return <AbsoluteFill>{voice&&<Audio src={staticFile(voice)}/>} {timeline.segments.map(s=><Sequence key={s.id} from={Math.round(s.start*fps)} durationInFrames={Math.max(1,Math.round((s.end-s.start)*fps))}><Scene segment={s}/></Sequence>)}{active&&<div style={{position:"absolute",left:220,right:220,bottom:45,textAlign:"center",font:"600 30px system-ui",color:"white"}}><span style={{background:"rgba(18,26,47,.9)",padding:"9px 18px"}}>{active.text}</span></div>}</AbsoluteFill>};
