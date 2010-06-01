/**********************************************************************
** This program is part of 'MOOSE', the
** Messaging Object Oriented Simulation Environment.
**           Copyright (C) 2003-2010 Upinder S. Bhalla. and NCBS
** It is made available under the terms of the
** GNU Lesser General Public License version 2.1
** See the file COPYING.LIB for the full notice.
**********************************************************************/
#ifndef _ARITH_H
#define _ARITH_H

class Arith: public Data
{
	friend void testCopyMsgOps();
	public: 
		Arith();
		void process( const ProcInfo* p, const Eref& e );

		/**
 		 * Inserts an event into the pendingEvents queue for spikes.
 		 */
		void addSpike( DataId synIndex, const double time );
		
		////////////////////////////////////////////////////////////////
		// Field assignment stuff.
		////////////////////////////////////////////////////////////////
		
		void setFunction( string v );
		string getFunction() const;
		void setOutput( double v );
		double getOutput() const;

		////////////////////////////////////////////////////////////////
		// Dest Func
		////////////////////////////////////////////////////////////////
		
		void arg1( double v );
		void arg2( double v );
		void eprocess( Eref e, const Qinfo* q, ProcPtr p );

		////////////////////////////////////////////////////////////////

		static const Cinfo* initCinfo();
	private:
		string function_; // String representation of operation to do.
		double output_; // Store the output so we can examine it.
		double arg1_;	// Argument 1
		double arg2_;	// Argument 2
};

#endif // _ARITH_H
