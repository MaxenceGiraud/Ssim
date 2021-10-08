#include <stdio.h>
#include <stdlib.h>
#include <vector>

int main() {
	const int dimx = 1024;		/* Image dimension */
	const int dimy = 1024;

	std::vector<size_t> I(dimx * dimy);
	for (int i = 0; i < dimx * dimy; ++i) I[i] = 0;

	const double e = 0;			/* brith and grow */
	const double k = 1.2;		/* Discretization */
	const double m = 0;			/* stability */
	const double step = 0.03;	/* Initial point step */

	for (double oy = -1.0; oy <= 1.0; oy += step) {
		for (double ox = -0.7; ox <= 1.3; ox += step) {
			if (ox == 0 || oy == 0) continue;			/* Avoid origin */
			double x = ox;
			double y = oy;
			for (size_t q = 0; q < 100000; ++q) {
				y = y + e * y + k * x * (x - 1) + m * x * y;
				x = x + y;
				if (labs(x) > 2 || labs(y) > 2) break;	/* the map diverge */
				double imx = (x - 0.3) * dimx / 2 + dimx / 2;
				double imy =  y        * dimy / 2 + dimy / 2;
				if (labs(x) > 1e-6 || labs(y) > 1e-6) {	/* Avoid origin */
					int ix = int(imx + 0.5);
					int iy = int(imy + 0.5);
					if (ix >= 0 && ix < dimx && iy >= 0 && iy < dimy)
						I[size_t(dimx) * (dimy - 1 - iy) + ix] ++;
				}
			}
		}
	}

	size_t maxd = I[0];			/* Compute max frequency */
	for (int i = 0; i < dimx * dimy; ++i)
		if (maxd < I[i]) maxd = I[i];

	FILE* fo = fopen("bogdanov_map.pgm", "wb");
	fprintf(fo, "P5\n%d %d\n255\n", dimx, dimy);
	for (int i = 0; i < dimx * dimy; ++i) {
		int v = I[i] == 0 ? 0 : int(32 + (256 - 32) * I[i] / maxd + 0.5); if (v > 255) v = 255;
		unsigned char b = 255 - (unsigned char)v;
		fwrite(&b, 1, 1, fo);
	}
	fclose(fo);
	return 0;
}