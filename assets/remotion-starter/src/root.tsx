import {Composition} from "remotion";
import {Video, type VideoProps} from "./video";
import timeline from "./timeline.json";

const durationSeconds=Math.max(1,timeline.duration+2);

export const Root=()=> <Composition id="AnyMaterialVideo" component={Video} width={1920} height={1080} fps={30} durationInFrames={Math.ceil(durationSeconds*30)} defaultProps={{timeline,voice:"assets/narration.wav"} satisfies VideoProps}/>;
