#include <cmath> 
#include <cstring>
#include <initializer_list>

const float PI        = 3.141592654;
const float TWO_PI    = 2.0f * PI;
const float DEG2RAD   = PI/180.0;
const float RAD2DEG   = 180.0/PI;

template<typename T> 
T lerp(const T &v0,const T &v1,float u) {return v0 + (v1 - v0) * u;}

struct vec3 
{
    typedef const vec3 & ref;
public:
    union
    {
        struct {float x, y, z;};
        struct {float r, g, b;};
        float data[3];
    };
       
    vec3(const float _x = 0, const float _y = 0 ,const float _z = 0) : 
        x(_x), y(_y),z(_z)
    {}
    vec3(std::initializer_list<float> l) 
    {
        std::memcpy(data,l.begin(),sizeof(data));
    }   

    vec3   operator-  () const {return vec3(-x,-y,-z);}
    float  operator*  (const vec3 &a)  const {return x * a.x + y * a.y + z * a.z;}
    vec3   operator*  (const float a)  const {return vec3( x * a, y * a, z * a);}
    vec3   operator+  (const vec3 &a)  const {return vec3(x + a.x, y + a.y, z+ a.z);}
    vec3   operator-  (const vec3 &a)  const {return vec3(x - a.x, y - a.y, z- a.z);}
    vec3 & operator+= (const vec3 &a)  {x += a.x; y += a.y; z += a.z; return *this;}
    vec3 & operator-= (const vec3 &a)  {x -= a.x; y -= a.y; z -= a.z; return *this;}
    vec3 & operator/= (const vec3 &a)  {x /= a.x; y /= a.y; z /= a.z; return *this;}
    vec3 & operator*= (const float a) {x *= a; y *= a; z *= a; return *this; }
  
    bool   operator== (const vec3 &a)  const {return compare(a);}
    bool   operator!= (const vec3 &a)  const {return !compare(a);}
    
    bool  compare(const vec3 &a) const {return ((x == a.x) && (y == a.y) && (z == a.z));}
    float length()  const {return std::sqrt(x * x + y * y + z * z);}
    vec3  cross(const vec3 &a) const
    {
        return vec3({y * a.z - z * a.y, z * a.x - x * a.z, x * a.y - y * a.x});
    }

    
    friend vec3 operator* (const float a, const vec3 b) {return vec3( b.x * a, b.y * a, b.z * a);}
};

struct mat
{
    typedef const mat & ref;
    union
    {
        float   d[4][4];
        float   data[16];
    };

    mat() : mat({1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1}) {}
    mat(std::initializer_list<float> l) {std::memcpy(data,l.begin(),sizeof(data));}   
    
    mat operator* (const mat &a) const
    {
        mat   dst;
        const float *m1  = reinterpret_cast<const float *>(this);
        const float *m2  = reinterpret_cast<const float *>(&a);
        float *ptr = reinterpret_cast<float *>(&dst);
        for(int i = 0; i < 4; i++)
        {
            for(int j = 0; j < 4; j++)
            {
                *ptr = m1[0]*m2[j]+m1[1]*m2[j+4]+m1[2]*m2[j+8]+m1[3]*m2[j+12];
                ptr++;
            }
            m1 += 4;
        }
        return dst;
    }
    mat & operator*= (const mat &a)
    {
        *this = (*this) * a;
        return *this;
    }
    void position(const vec3 &v) 
    {
        d[0][3] = v.x;
        d[1][3] = v.y;
        d[2][3] = v.z;
    }
    vec3 position() const {return {d[0][3],d[1][3],d[2][3]};}

    static mat rotate(const vec3 &v)
    {
        auto sx = std::sin(v.x); auto cx = std::cos(v.x);
        auto sy = std::sin(v.y); auto cy = std::cos(v.y);
        auto sz = std::sin(v.z); auto cz = std::cos(v.z);
        return 
            mat({1,0,0,0,0,cx,-sx,0,0,sx,cx,0,0,0,0,1}) *
            mat({cy,0,sy,0,0,1,0,0,-sy,0,cy,0,0,0,0,1}) *
            mat({cz,-sz,0,0,sz,cz,0,0,0,0,1,0,0,0,0,1}); 
    }
    static mat scale(const vec3 &v)     {return {v.x,0,0,0,0,v.y,0,0,0,0,v.z,0,0,0,0,1};}
    static mat translate(const vec3 &v) {return {1,0,0,v.x,0,1,0,v.y,0,0,1,v.z,0,0,0,1};}
    static mat perspective(float fov,float aspect,float n,float f)
    {
        float h = std::tan(fov * DEG2RAD * .5);
        float w = h * aspect;
        float dz = f-n;
        return mat({1.0f/w,0,0,0,0,1.0f/h,0,0,0,0,-(f+n)/dz,-2.0f*f*n/dz,0,0,-1.0f,0});
    }
};