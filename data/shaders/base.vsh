attribute vec3 position;
attribute vec2 texcoord;
attribute vec3 normal;

uniform   mat4 modelView;
uniform   mat4 prjView;

varying vec2 v_tex;
varying vec3 v_norm;
varying vec3 v_light;
varying vec3 v_eye; 

const vec3 light_position = vec3(-20,0,0);
const vec3 eye_position   = vec3(0,0,0);

void main()
{
    mat3 normalMatrix = mat3(modelView[0].xyz,modelView[1].xyz,modelView[2].xyz);

	vec4 p4 = vec4(position,1);
	vec3 view_pos   = vec3(p4 * modelView);
    
    v_light  = normalize(light_position - view_pos);
    v_eye    = normalize(eye_position   - view_pos);
    v_norm   = normal * normalMatrix;
	v_tex    = texcoord;
	
	gl_Position = p4 * modelView * prjView;
}

