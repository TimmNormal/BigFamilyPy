MAX = 100

REAL_MAX = MAX + 1


for a in range(1,REAL_MAX):
	print(a)
	for b in range(1,REAL_MAX):
		for c in range(1,REAL_MAX):
			for d in range(1,REAL_MAX):
				for f in range(1,REAL_MAX):
					for i in range(1,REAL_MAX):
						for g in range(1,REAL_MAX):
							for h in range(1,REAL_MAX):
								for t in range(1,REAL_MAX):
									if (a*a + b*b + c*c) == (d*d + f*f + i*i) == (g*g + h*h + t*t) == (a*a + d*d + g*g) ==(b*b + f*f + h*h) == (c*c + i*i + t*t) == (a^2 + f^2 + t^2) == (c^2 + f^2 + g^2) and a!=b!=c!=d!=f!=i!=g!=h!=t:
										print(a,b,c,d,f,i,g,h,t)
										print((a*a + b*b + c*c))
										print((d^2 + f^2 + i^2))
										print((g^2 + h^2 + t^2))
										print((a^2 + d^2 + g^2))
										print((b^2 + f^2 + h^2))
										print((c^2 + i^2 + t^2))
										print((a^2 + f^2 + t^2))
										print((c^2 + f^2 + g^2))
										quit()