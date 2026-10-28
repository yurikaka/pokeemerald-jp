.syntax unified
.cpu arm7tdmi
.thumb
.section .text.remote_official_sender, "ax", %progbits
.align 2
.global RemoteOfficialSenderCopy
.type RemoteOfficialSenderCopy, %function
.thumb_func
RemoteOfficialSenderCopy:
	push {r4, r5, r6, lr}
	sub sp, #4
	lsls r0, r0, #0x18
	lsrs r2, r0, #0x18
	lsls r0, r2, #2
	adds r0, r0, r2
	lsls r0, r0, #3
	ldr r1, _081BF0E4
	adds r5, r0, r1
	movs r1, #0
	ldrsh r0, [r5, r1]
	cmp r0, #0xa
	bls _081BF0D8
	b _081BF272
_081BF0D8:
	lsls r0, r0, #2
	ldr r1, _081BF0E8
	adds r0, r0, r1
	ldr r0, [r0]
	mov pc, r0
	.align 2, 0
_081BF0E4: .4byte 0x03005B68
_081BF0E8: .4byte _081BF0EC
_081BF0EC: @ jump table
	.4byte _081BF118 @ case 0
	.4byte _081BF122 @ case 1
	.4byte _081BF140 @ case 2
	.4byte _081BF272 @ case 3
	.4byte _081BF15C @ case 4
	.4byte _081BF194 @ case 5
	.4byte _081BF200 @ case 6
	.4byte _081BF236 @ case 7
	.4byte _081BF23A @ case 8
	.4byte _081BF258 @ case 9
	.4byte _081BF262 @ case 10
_081BF118:
	movs r0, #5
	@ Keep the existing screen during connection.
	movs r0, #1
	b _081BF270
_081BF122:
	ldr r0, _081BF13C
	ldrh r1, [r0, #0x2e]
	movs r0, #1
	ands r0, r1
	cmp r0, #0
	bne _081BF130
	b _081BF272
_081BF130:
	movs r0, #0
	@ Keep the existing screen during connection.
	movs r0, #2
	b _081BF270
	.align 2, 0
_081BF13C: .4byte 0x03002360
_081BF140:
	ldr r0, _081BF158
	ldrh r1, [r0, #0x2e]
	movs r0, #1
	ands r0, r1
	cmp r0, #0
	bne _081BF14E
	b _081BF272
_081BF14E:
	movs r0, #1
	@ Keep the existing screen during connection.
	movs r0, #4
	b _081BF270
	.align 2, 0
_081BF158: .4byte 0x03002360
_081BF15C:
	ldr r0, _081BF180
	ldr r1, _081BF184
	str r1, [r0]
	ldr r2, _081BF188
	ldr r0, _081BF18C
	subs r0, r0, r1
	str r0, [r2]
	ldr r0, _081BF190
	str r1, [r0, #0x28]
	adds r1, r0, #0
	adds r1, #0x4b
	movs r4, #0
	strb r4, [r1]
	bl RemoteStub_GetGlyphWidthFont6
	strh r4, [r5, #2]
	movs r0, #5
	b _081BF270
	.align 2, 0
_081BF180: .4byte 0x03006070
_081BF184: .4byte RemoteReceiverImageStart
_081BF188: .4byte 0x03006078
_081BF18C: .4byte RemoteReceiverImageEnd
_081BF190: .4byte 0x03006080
_081BF194:
	ldr r0, _081BF1DC
	ldrb r6, [r0, #0x18]
	adds r4, r0, #0
	cmp r6, #0
	bne _081BF1EC
	ldr r0, [r4, #0x1c]
	ldr r1, _081BF1E0
	ands r0, r1
	cmp r0, r1
	bne _081BF1EC
	ldrh r0, [r5, #2]
	adds r0, #1
	strh r0, [r5, #2]
	lsls r0, r0, #0x10
	asrs r0, r0, #0x10
	cmp r0, #0xb4
	ble _081BF1F0
	movs r0, #2
	@ Keep the existing screen during connection.
	ldr r0, _081BF1E4
	ldr r1, [r0]
	adds r1, #0xc0
	ldr r0, _081BF1E8
	ldr r2, [r0]
	subs r2, #0xc0
	movs r0, #1
	str r0, [sp]
	adds r0, r4, #0
	movs r3, #4
	bl RemoteStub_sub_081BA808
	strh r6, [r5, #2]
	movs r0, #6
	b _081BF270
	.align 2, 0
_081BF1DC: .4byte 0x03006080
_081BF1E0: .4byte 0x00020200
_081BF1E4: .4byte 0x03006070
_081BF1E8: .4byte 0x03006078
_081BF1EC:
	movs r0, #0
	strh r0, [r5, #2]
_081BF1F0:
	adds r0, r4, #0
	bl RemoteStub_sub_081BA3A8
	ldr r1, _081BF1FC
	str r0, [r1]
	b _081BF272
	.align 2, 0
_081BF1FC: .4byte 0x03006074
_081BF200:
	ldr r4, _081BF220
	adds r0, r4, #0
	bl RemoteStub_sub_081BA3A8
	ldr r1, _081BF224
	str r0, [r1]
	adds r0, r4, #0
	bl RemoteStub_sub_081BA8CC
	cmp r0, #0
	beq _081BF228
	movs r0, #3
	@ Keep the existing screen during connection.
	movs r0, #7
	b _081BF270
	.align 2, 0
_081BF220: .4byte 0x03006080
_081BF224: .4byte 0x03006074
_081BF228:
	ldrb r1, [r4, #0x1e]
	movs r0, #2
	ands r0, r1
	cmp r0, #0
	bne _081BF272
	movs r0, #9
	b _081BF270
_081BF236:
	movs r0, #8
	b _081BF270
_081BF23A:
	ldr r0, _081BF254
	ldrh r1, [r0, #0x2e]
	movs r0, #1
	ands r0, r1
	cmp r0, #0
	beq _081BF272
	adds r0, r2, #0
	bl RemoteStub_DestroyTask
	bl RemoteStub_DoSoftReset
	b _081BF272
	.align 2, 0
_081BF254: .4byte 0x03002360
_081BF258:
	movs r0, #4
	@ Keep the existing screen during connection.
	movs r0, #0xa
	b _081BF270
_081BF262:
	ldr r0, _081BF27C
	ldrh r1, [r0, #0x2e]
	movs r0, #1
	ands r0, r1
	cmp r0, #0
	beq _081BF272
	movs r0, #0
_081BF270:
	strh r0, [r5]
_081BF272:
	add sp, #4
	pop {r4, r5, r6}
	pop {r0}
	bx r0
	.align 2, 0
_081BF27C: .4byte 0x03002360

.align 2
.thumb_func
RemoteStub_sub_081BAA20:
    push {r3}
    ldr r3, =0x81baa21
    mov ip, r3
    pop {r3}
    bx ip
.ltorg

.align 2
.thumb_func
RemoteStub_GetGlyphWidthFont6:
    push {r3}
    ldr r3, =0x81ba36d
    mov ip, r3
    pop {r3}
    bx ip
.ltorg

.align 2
.thumb_func
RemoteStub_sub_081BA808:
    push {r3}
    ldr r3, =0x81ba809
    mov ip, r3
    pop {r3}
    bx ip
.ltorg

.align 2
.thumb_func
RemoteStub_sub_081BA3A8:
    push {r3}
    ldr r3, =0x81ba3a9
    mov ip, r3
    pop {r3}
    bx ip
.ltorg

.align 2
.thumb_func
RemoteStub_sub_081BA8CC:
    push {r3}
    ldr r3, =0x81ba8cd
    mov ip, r3
    pop {r3}
    bx ip
.ltorg

.align 2
.thumb_func
RemoteStub_DestroyTask:
    push {r3}
    ldr r3, =0x80a8965
    mov ip, r3
    pop {r3}
    bx ip
.ltorg

.align 2
.thumb_func
RemoteStub_DoSoftReset:
    push {r3}
    ldr r3, =0x80008f5
    mov ip, r3
    pop {r3}
    bx ip
.ltorg
