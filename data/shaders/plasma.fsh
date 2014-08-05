varying vec2  v_tex;
uniform float time;
uniform sampler2D texture0;

const float PI    = 3.14159;
const int zoom    = 50;
const float speed = 4.0;
float fScale      = 1.25;

void main()
{
  	vec4 tcol = texture2D(texture0, v_tex);
  
	vec2 p= v_tex;
	float ct = time * speed;
	
	for(int i=1; i<zoom; i++) 
	{
		vec2 newp=p;
		newp.x+=0.25/float(i)*cos(float(i)*p.y+time*cos(ct)*0.3/40.0+0.03*float(i))*fScale+10.0;		
		newp.y+=0.5 /float(i)*cos(float(i)*p.x+time*ct*0.3/50.0+0.03*float(i+10))*fScale+15.0;
		p=newp;
	}
	
	vec3 col=vec3(0.5*sin(3.0*p.x)+0.5,0.5*sin(3.0*p.y)+0.5,sin(p.x+p.y));
	gl_FragColor=vec4(col, 1.0) * tcol;
	
}