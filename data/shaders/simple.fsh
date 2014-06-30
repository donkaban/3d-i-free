uniform sampler2D texture0;
uniform sampler2D texture1;

varying vec2 v_tex;
varying vec3 v_norm;
varying vec3 v_light;
varying vec3 v_eye; 

const float specular_power = 35.0;

void main()
{
    vec4 col = texture2D(texture0, v_tex);
   	float lambert_factor = max(dot(v_norm,v_light),0.);
    float phong_factor   = pow(max(dot(v_norm,normalize(v_light + v_eye)), 0.),specular_power);
    col *= lambert_factor;
    col += phong_factor;
    col.a = 1.0;
  	gl_FragColor = col;
}
