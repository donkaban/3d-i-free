uniform sampler2D texture0;
uniform sampler2D texture1;

varying vec2  v_tex;
varying vec3 v_normal;

void main()
{
    vec4 col1 = texture2D(texture0, v_tex);
    vec4 col2 = texture2D(texture1, v_tex);
    col2.a = .6;
    gl_FragColor = col1 * vec4(v_normal,1.0);
}
