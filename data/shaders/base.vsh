attribute vec3 position;
attribute vec2 texcoord;
attribute vec3 normal;

uniform   mat4 modelView;
uniform   mat4 prjView;

varying   vec2 v_tex;
varying   vec3 v_normal;

void main()
{
    v_tex=texcoord;
    v_normal = normal;
    gl_Position = vec4(position,1) * modelView * prjView;
}

