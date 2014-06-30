attribute vec3 position;
attribute vec2 texcoord;
attribute vec3 normal;

uniform   mat4 modelView;
uniform   mat4 prjView;

varying vec2 v_tex;
varying vec3 v_norm;
varying vec3 v_light;
varying vec3 v_eye; 

const vec3 light_position = vec3(0,10,0);
const vec3 eye_position   = vec3(0,0,0);

void main()
{
	vec4 p4 = vec4(position,1);
	vec4 n4 = vec4(normal,0);

	vec3 view_pos   = vec3(p4 * modelView);
    
    v_light  = normalize(light_position - view_pos);
    v_eye    = normalize(eye_position   - view_pos);
    v_norm   = vec3(n4 * modelView);
	v_tex    = texcoord;
	
	gl_Position = p4 * modelView * prjView;
}

